#!/usr/bin/env python3
import argparse
import os
import sys
from datetime import datetime


def main():
    p = argparse.ArgumentParser(description="Search and optionally download Sentinel-2 L2A scenes using sentinelsat.")
    p.add_argument("--user", required=True, help="Copernicus Open Access Hub username")
    p.add_argument("--password", required=True, help="Copernicus Open Access Hub password")
    p.add_argument("--aoi", required=True, help="AOI in GeoJSON file (Polygon/MultiPolygon) or WKT string")
    p.add_argument("--start", required=True, help="Start date (YYYY-MM-DD)")
    p.add_argument("--end", required=True, help="End date (YYYY-MM-DD)")
    p.add_argument("--max-results", type=int, default=4, help="Max number of scenes to download/search (default: 4)")
    p.add_argument("--cloud-max", type=float, default=20.0, help="Max cloud cover percent (default: 20)")
    p.add_argument("--out", default="data/s2", help="Output directory for downloads")
    p.add_argument("--search-only", action="store_true", help="Only list results; do not download")
    args = p.parse_args()

    try:
        from sentinelsat import SentinelAPI, geojson_to_wkt
    except Exception as e:
        print("ERROR: sentinelsat is required. pip install sentinelsat", file=sys.stderr)
        sys.exit(2)

    # AOI parsing
    aoi_wkt = args.aoi
    if os.path.exists(args.aoi) and args.aoi.lower().endswith((".json", ".geojson")):
        import json as _json
        with open(args.aoi, "r") as f:
            gj = _json.load(f)
        aoi_wkt = geojson_to_wkt(gj)

    api = SentinelAPI(args.user, args.password, "https://apihub.copernicus.eu/apihub")

    date_range = (datetime.fromisoformat(args.start), datetime.fromisoformat(args.end))
    products = api.query(
        area=aoi_wkt,
        date=date_range,
        platformname="Sentinel-2",
        producttype="S2MSI2A",
        cloudcoverpercentage=(0, args.cloud_max),
        order_by="-beginposition"
    )

    if not products:
        print("No products found for the given criteria.")
        return

    # Convert to DataFrame for pretty print
    df = api.to_dataframe(products)
    df = df.sort_values("beginposition", ascending=False)
    print(df[["title", "beginposition", "cloudcoverpercentage"]].head(args.max_results))

    if args.search_only:
        return

    os.makedirs(args.out, exist_ok=True)
    to_download = df.head(args.max_results).index.tolist()
    print(f"Downloading {len(to_download)} products to {args.out}...")
    api.download_all(to_download, directory_path=args.out)


if __name__ == "__main__":
    main()
