#!/usr/bin/env python3
import argparse
import os
import sys


def main():
    p = argparse.ArgumentParser(description="Rasterize CORINE/CLC vector labels to match a reference raster grid.")
    p.add_argument("--clc", required=True, help="Path to CORINE/CLC vector file (e.g., .gpkg/.shp)")
    p.add_argument("--ref", required=True, help="Path to reference raster (GeoTIFF) to match CRS, transform, and shape")
    p.add_argument("--out", required=True, help="Output label raster (GeoTIFF)")
    p.add_argument("--class-field", default="code_18", help="Attribute field with class codes (default: code_18)")
    p.add_argument("--burn-value", type=int, default=None, help="Optional fixed burn value (overrides per-feature class field)")
    args = p.parse_args()

    try:
        import geopandas as gpd
        import rasterio as rio
        from rasterio.features import rasterize
        from shapely.geometry import box
    except Exception as e:
        print("ERROR: Requires geopandas, rasterio, shapely.", file=sys.stderr)
        sys.exit(2)

    clc = gpd.read_file(args.clc)
    with rio.open(args.ref) as src:
        dst_profile = src.profile.copy()
        transform = src.transform
        crs = src.crs
        out_shape = (src.height, src.width)
        bounds = src.bounds

    # Reproject to match raster CRS
    clc = clc.to_crs(crs)

    # Clip CLC to raster bounds for speed
    bbox = gpd.GeoSeries([box(*bounds)], crs=crs)
    clc_clip = gpd.overlay(clc, gpd.GeoDataFrame(geometry=bbox), how='intersection')

    # Prepare shapes
    if args.burn_value is not None:
        shapes = ((geom, int(args.burn_value)) for geom in clc_clip.geometry if geom is not None)
    else:
        field = args.class_field
        if field not in clc_clip.columns:
            raise SystemExit(f"Class field '{field}' not found in CLC vector attributes.")
        shapes = ((geom, int(val)) for geom, val in zip(clc_clip.geometry, clc_clip[field]) if geom is not None)

    labels = rasterize(shapes=shapes, out_shape=out_shape, transform=transform, fill=0, dtype='uint16')

    dst_profile.update(count=1, dtype='uint16')
    os.makedirs(os.path.dirname(args.out) or '.', exist_ok=True)
    with rio.open(args.out, 'w', **dst_profile) as dst:
        dst.write(labels, 1)
    print(f"Wrote labels: {args.out}")


if __name__ == "__main__":
    main()
