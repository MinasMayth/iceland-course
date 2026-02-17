#!/usr/bin/env python3
"""
Lab 3.2: Data Preprocessing & CORINE Label Extraction
=====================================================

This script processes Sentinel-2 imagery and CORINE Land Cover data to create
training datasets for machine learning models.

Usage:
    python preprocess_corine_s2.py --s2_tile <path_to_safe_dir> [options]

Example:
    python preprocess_corine_s2.py --s2_tile /path/to/S2A_MSIL2A_*.SAFE --patch_size 3 --max_patches 50000

Author: ML-EO Course, Juelich Supercomputing Centre
Date: 2026
"""

import os
import sys
import argparse
import json
import subprocess
from pathlib import Path
import numpy as np
from osgeo import gdal
import matplotlib.pyplot as plt
from datetime import datetime

# GDAL configuration
gdal.UseExceptions()
os.environ['GDAL_CACHEMAX'] = '2048'  # Increase cache for large files


class Logger:
    """Simple logger for student-friendly output"""
    
    def __init__(self, verbose=True):
        self.verbose = verbose
    
    def section(self, text):
        """Print a section header"""
        print("\n" + "=" * 70)
        print(text)
        print("=" * 70)
    
    def info(self, text, indent=0):
        """Print info message"""
        if self.verbose:
            prefix = "  " * indent
            print(f"{prefix}✓ {text}")
    
    def warn(self, text, indent=0):
        """Print warning message"""
        prefix = "  " * indent
        print(f"{prefix}⚠ {text}")
    
    def error(self, text, indent=0):
        """Print error message"""
        prefix = "  " * indent
        print(f"{prefix}❌ {text}")
    
    def progress(self, text, indent=0):
        """Print progress message"""
        if self.verbose:
            prefix = "  " * indent
            print(f"{prefix}  {text}", end='\r')


class CORINEProcessor:
    """Handles CORINE Land Cover data operations"""
    
    # CORINE class descriptions for reference
    # Note: CORINE raster uses simplified codes 1-44, mapped to full CLC codes
    CORINE_CLASSES = {
        # Simplified codes (1-44) used in raster
        1: "Continuous urban fabric",
        2: "Discontinuous urban fabric",
        3: "Industrial or commercial units",
        4: "Road and rail networks",
        5: "Port areas",
        6: "Airports",
        7: "Mineral extraction sites",
        8: "Dump sites",
        9: "Construction sites",
        10: "Green urban areas",
        11: "Sport and leisure facilities",
        12: "Non-irrigated arable land",
        13: "Permanently irrigated land",
        14: "Rice fields",
        15: "Vineyards",
        16: "Fruit trees and berry plantations",
        17: "Olive groves",
        18: "Pastures",
        19: "Annual crops with permanent crops",
        20: "Complex cultivation patterns",
        21: "Agriculture with natural vegetation",
        22: "Agro-forestry areas",
        23: "Broad-leaved forest",
        24: "Coniferous forest",
        25: "Mixed forest",
        26: "Natural grasslands",
        27: "Moors and heathland",
        28: "Sclerophyllous vegetation",
        29: "Transitional woodland-shrub",
        30: "Beaches, dunes, sands",
        31: "Bare rocks",
        32: "Sparsely vegetated areas",
        33: "Burnt areas",
        34: "Glaciers and perpetual snow",
        35: "Inland marshes",
        36: "Peat bogs",
        37: "Salt marshes",
        38: "Salines",
        39: "Intertidal flats",
        40: "Water courses",
        41: "Water bodies",
        42: "Coastal lagoons",
        43: "Estuaries",
        44: "Sea and ocean",
        48: "No data"
    }
    
    def __init__(self, corine_path, logger):
        self.corine_path = Path(corine_path)
        self.logger = logger
        self.ds = None
    
    def open(self):
        """Open CORINE raster dataset"""
        try:
            self.ds = gdal.Open(str(self.corine_path), gdal.GA_ReadOnly)
            if self.ds is None:
                raise Exception(f"Could not open CORINE file: {self.corine_path}")
            
            self.logger.info(f"CORINE dataset opened: {self.corine_path.name}")
            self.logger.info(f"Dimensions: {self.ds.RasterXSize} x {self.ds.RasterYSize}", indent=1)
            self.logger.info(f"Resolution: 100m x 100m", indent=1)
            
            return True
        except Exception as e:
            self.logger.error(f"Failed to open CORINE: {e}")
            return False
    
    def get_info(self):
        """Get CORINE dataset information"""
        if self.ds is None:
            return None
        
        gt = self.ds.GetGeoTransform()
        return {
            'width': self.ds.RasterXSize,
            'height': self.ds.RasterYSize,
            'projection': self.ds.GetProjection(),
            'geotransform': gt,
            'ulx': gt[0],
            'uly': gt[3],
            'lrx': gt[0] + self.ds.RasterXSize * gt[1],
            'lry': gt[3] + self.ds.RasterYSize * gt[5]
        }
    
    def align_to_s2(self, s2_path, output_path):
        """
        Align CORINE to match Sentinel-2 tile geometry
        
        Parameters:
        -----------
        s2_path : Path
            Sentinel-2 reference file
        output_path : Path
            Output aligned CORINE file
        
        Returns:
        --------
        bool : Success status
        """
        try:
            self.logger.info(f"Aligning CORINE to S2 tile...")
            
            # Open S2 to get target parameters
            s2_ds = gdal.Open(str(s2_path), gdal.GA_ReadOnly)
            if s2_ds is None:
                raise Exception(f"Could not open S2 file: {s2_path}")
            
            # Get S2 geometry
            target_srs = s2_ds.GetProjection()
            gt = s2_ds.GetGeoTransform()
            ulx, xres, _, uly, _, yres = gt
            lrx = ulx + (s2_ds.RasterXSize * xres)
            lry = uly + (s2_ds.RasterYSize * yres)
            
            self.logger.info(f"Target extent: {ulx:.0f}, {lry:.0f}, {lrx:.0f}, {uly:.0f}", indent=1)
            self.logger.info(f"Target resolution: {xres}m", indent=1)
            
            s2_ds = None
            
            # Use gdalwarp command-line tool for more reliable reprojection
            # CORINE is in EPSG:3035 (ETRS89-LAEA), S2 is typically in UTM
            cmd = [
                'gdalwarp',
                '-s_srs', 'EPSG:3035',
                '-t_srs', 'EPSG:32633',  # UTM zone from target
                '-te', str(ulx), str(lry), str(lrx), str(uly),
                '-tr', str(xres), str(abs(yres)),
                '-r', 'near',
                '-co', 'COMPRESS=LZW',
                '-co', 'TILED=YES',
                '-overwrite',
                str(self.corine_path),
                str(output_path)
            ]
            
            self.logger.info(f"Running gdalwarp...", indent=1)
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode != 0:
                raise Exception(f"gdalwarp failed: {result.stderr}")
            
            self.logger.info(f"CORINE aligned successfully: {output_path.name}")
            return True
            
        except Exception as e:
            self.logger.error(f"Alignment failed: {e}")
            return False
    
    def analyze_classes(self, data_subset):
        """Analyze CORINE classes in a data subset"""
        unique, counts = np.unique(data_subset, return_counts=True)
        
        # Filter out no-data
        mask = (unique > 0) & (unique < 255)
        unique = unique[mask]
        counts = counts[mask]
        
        # Sort by frequency
        sort_idx = np.argsort(counts)[::-1]
        unique = unique[sort_idx]
        counts = counts[sort_idx]
        
        total = counts.sum()
        
        return [(int(cls), int(cnt), (cnt / total) * 100) 
                for cls, cnt in zip(unique, counts)]
    
    def close(self):
        """Close CORINE dataset"""
        if self.ds is not None:
            self.ds = None


class Sentinel2Processor:
    """Handles Sentinel-2 data operations"""
    
    def __init__(self, safe_path, logger):
        self.safe_path = Path(safe_path)
        self.logger = logger
        self.bands = ['B02', 'B03', 'B04', 'B08']  # Blue, Green, Red, NIR
        self.resolution = '10m'
    
    def find_bands(self):
        """Find band files in SAFE directory"""
        band_paths = {}
        
        for band_name in self.bands:
            pattern = f"**/R{self.resolution}/*_{band_name}_{self.resolution}.jp2"
            matches = list(self.safe_path.glob(pattern))
            
            if matches:
                band_paths[band_name] = matches[0]
                self.logger.info(f"Found {band_name}: {matches[0].name}", indent=1)
            else:
                self.logger.warn(f"{band_name} not found", indent=1)
        
        return band_paths
    
    def stack_bands(self, band_paths, output_path):
        """
        Stack Sentinel-2 bands into multi-band GeoTIFF
        
        Parameters:
        -----------
        band_paths : dict
            Dictionary of band name -> file path
        output_path : Path
            Output stacked file
        
        Returns:
        --------
        bool : Success status
        """
        try:
            self.logger.info(f"Stacking S2 bands...")
            
            # Open first band to get metadata
            first_band = list(band_paths.values())[0]
            ds_first = gdal.Open(str(first_band), gdal.GA_ReadOnly)
            
            if ds_first is None:
                raise Exception(f"Could not open {first_band}")
            
            # Get dimensions
            x_size = ds_first.RasterXSize
            y_size = ds_first.RasterYSize
            projection = ds_first.GetProjection()
            geotransform = ds_first.GetGeoTransform()
            
            self.logger.info(f"Dimensions: {x_size} x {y_size}", indent=1)
            
            # Create output file
            driver = gdal.GetDriverByName('GTiff')
            out_ds = driver.Create(
                str(output_path),
                x_size,
                y_size,
                len(band_paths),
                gdal.GDT_UInt16,
                options=['COMPRESS=LZW', 'TILED=YES', 'BIGTIFF=YES']
            )
            
            out_ds.SetProjection(projection)
            out_ds.SetGeoTransform(geotransform)
            
            # Write each band
            for i, (band_name, band_path) in enumerate(band_paths.items(), start=1):
                self.logger.progress(f"Processing {band_name}...", indent=1)
                
                ds_band = gdal.Open(str(band_path), gdal.GA_ReadOnly)
                data = ds_band.GetRasterBand(1).ReadAsArray()
                
                out_band = out_ds.GetRasterBand(i)
                out_band.WriteArray(data)
                out_band.SetDescription(band_name)
                out_band.FlushCache()
                
                ds_band = None
            
            # Close datasets
            out_ds = None
            ds_first = None
            
            print()  # Clear progress line
            self.logger.info(f"Bands stacked successfully: {output_path.name}")
            return True
            
        except Exception as e:
            self.logger.error(f"Band stacking failed: {e}")
            return False


class PatchExtractor:
    """Extract training patches from aligned S2 and CORINE data"""
    
    def __init__(self, s2_path, corine_path, logger):
        self.s2_path = Path(s2_path)
        self.corine_path = Path(corine_path)
        self.logger = logger
    
    def extract(self, patch_size=3, stride=None, max_patches=50000, output_dir=None):
        """
        Extract patches with CORINE labels
        
        Parameters:
        -----------
        patch_size : int
            Size of patches (e.g., 3 = 3x3 pixels = 30m x 30m at 10m resolution)
        stride : int
            Stride for patch extraction (None = no overlap)
        max_patches : int
            Maximum number of patches to extract
        output_dir : Path
            Output directory for patches
        
        Returns:
        --------
        tuple : (patches, labels, metadata) or None
        """
        try:
            self.logger.section("Extracting Training Patches")
            
            # Open datasets
            s2_ds = gdal.Open(str(self.s2_path), gdal.GA_ReadOnly)
            corine_ds = gdal.Open(str(self.corine_path), gdal.GA_ReadOnly)
            
            if s2_ds is None or corine_ds is None:
                raise Exception("Could not open input files")
            
            # Get dimensions
            n_bands = s2_ds.RasterCount
            height = s2_ds.RasterYSize
            width = s2_ds.RasterXSize
            
            self.logger.info(f"S2 dimensions: {width} x {height} x {n_bands} bands")
            self.logger.info(f"Patch size: {patch_size}x{patch_size} ({patch_size * 10}m x {patch_size * 10}m)")
            
            # Set stride
            if stride is None:
                stride = patch_size
            
            self.logger.info(f"Stride: {stride} (overlap: {patch_size - stride} pixels)")
            
            # Read data in chunks to manage memory
            chunk_size = 2000  # Process 2000x2000 pixels at a time
            
            patches = []
            labels = []
            coords = []
            
            total_possible = ((height - patch_size) // stride + 1) * ((width - patch_size) // stride + 1)
            self.logger.info(f"Maximum possible patches: {total_possible:,}")
            self.logger.info(f"Will extract up to: {max_patches:,}")
            
            print()
            
            # Iterate over image in chunks
            for y_chunk in range(0, height, chunk_size):
                for x_chunk in range(0, width, chunk_size):
                    
                    # Calculate chunk boundaries
                    y_end = min(y_chunk + chunk_size, height)
                    x_end = min(x_chunk + chunk_size, width)
                    
                    # Skip if chunk is too small for patches
                    if (y_end - y_chunk) < patch_size or (x_end - x_chunk) < patch_size:
                        continue
                    
                    # Read chunk
                    s2_chunk = np.zeros((y_end - y_chunk, x_end - x_chunk, n_bands), dtype=np.uint16)
                    for i in range(n_bands):
                        band = s2_ds.GetRasterBand(i + 1)
                        s2_chunk[:, :, i] = band.ReadAsArray(x_chunk, y_chunk, x_end - x_chunk, y_end - y_chunk)
                    
                    corine_chunk = corine_ds.GetRasterBand(1).ReadAsArray(x_chunk, y_chunk, x_end - x_chunk, y_end - y_chunk)
                    
                    # Extract patches from chunk
                    for y_local in range(0, y_end - y_chunk - patch_size + 1, stride):
                        for x_local in range(0, x_end - x_chunk - patch_size + 1, stride):
                            
                            # Extract patch
                            patch = s2_chunk[y_local:y_local + patch_size, x_local:x_local + patch_size, :]
                            
                            # Get center pixel label
                            center_y = y_local + patch_size // 2
                            center_x = x_local + patch_size // 2
                            label = corine_chunk[center_y, center_x]
                            
                            # Skip invalid CORINE labels
                            # Valid CORINE classes are 1-44 in the raster
                            if label < 1 or label > 44:  # Invalid/no-data
                                continue
                            
                            if np.any(patch == 0):  # Clouds/missing data
                                continue
                            
                            # Store patch
                            patches.append(patch)
                            labels.append(label)
                            coords.append((y_chunk + y_local, x_chunk + x_local))
                            
                            if len(patches) >= max_patches:
                                break
                        
                        if len(patches) >= max_patches:
                            break
                    
                    # Progress update
                    progress = (y_chunk / height) * 100
                    self.logger.progress(
                        f"Progress: {progress:.1f}% | Extracted: {len(patches):,} patches",
                        indent=0
                    )
                    
                    if len(patches) >= max_patches:
                        break
                
                if len(patches) >= max_patches:
                    self.logger.info(f"\nReached maximum patches limit: {max_patches:,}")
                    break
            
            # Close datasets
            s2_ds = None
            corine_ds = None
            
            print()
            self.logger.info(f"Extracted {len(patches):,} patches")
            
            if len(patches) == 0:
                self.logger.warn("No valid patches extracted!")
                return None, None, None
            
            # Convert to arrays
            patches = np.array(patches, dtype=np.uint16)
            labels = np.array(labels, dtype=np.uint8)
            
            # Analyze label distribution
            unique_labels, counts = np.unique(labels, return_counts=True)
            
            self.logger.info(f"\nPatch Statistics:")
            self.logger.info(f"  Shape: {patches.shape}", indent=1)
            self.logger.info(f"  Data type: {patches.dtype}", indent=1)
            self.logger.info(f"  Memory: {patches.nbytes / (1024**2):.1f} MB", indent=1)
            self.logger.info(f"  Unique classes: {len(unique_labels)}", indent=1)
            
            self.logger.info(f"\nTop 10 land cover classes:", indent=0)
            sort_idx = np.argsort(counts)[::-1][:10]
            for idx in sort_idx:
                cls = unique_labels[idx]
                cnt = counts[idx]
                pct = (cnt / len(labels)) * 100
                class_name = CORINEProcessor.CORINE_CLASSES.get(cls, "Unknown")
                self.logger.info(f"  Class {cls:3d} ({class_name[:30]:30s}): {cnt:6d} ({pct:5.1f}%)", indent=1)
            
            # Create metadata
            metadata = {
                's2_tile': self.s2_path.stem,
                'corine_file': self.corine_path.name,
                'patch_size': patch_size,
                'stride': stride,
                'n_patches': len(patches),
                'n_bands': patches.shape[3],
                'n_classes': len(unique_labels),
                'label_distribution': {int(k): int(v) for k, v in zip(unique_labels, counts)},
                'extraction_date': datetime.now().isoformat(),
                'patch_shape': list(patches.shape),
                'bands': ['B02', 'B03', 'B04', 'B08']
            }
            
            # Save if output directory provided
            if output_dir:
                self.save_patches(patches, labels, metadata, output_dir)
            
            return patches, labels, metadata
            
        except Exception as e:
            self.logger.error(f"Patch extraction failed: {e}")
            import traceback
            traceback.print_exc()
            return None, None, None
    
    def save_patches(self, patches, labels, metadata, output_dir):
        """Save extracted patches and metadata"""
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        
        base_name = f"patches_{metadata['s2_tile']}"
        
        # Save patches (compressed)
        patches_file = output_dir / f"{base_name}_data.npz"
        np.savez_compressed(patches_file, patches=patches, labels=labels)
        
        # Save metadata
        metadata_file = output_dir / f"{base_name}_metadata.json"
        with open(metadata_file, 'w') as f:
            json.dump(metadata, f, indent=2)
        
        self.logger.info(f"\nData saved:")
        self.logger.info(f"  Patches: {patches_file}", indent=1)
        self.logger.info(f"  Size: {patches_file.stat().st_size / (1024**2):.1f} MB", indent=2)
        self.logger.info(f"  Metadata: {metadata_file}", indent=1)


def visualize_samples(patches, labels, output_path=None):
    """Create visualization of sample patches"""
    
    # Select diverse samples
    unique_labels = np.unique(labels)
    n_samples = min(6, len(unique_labels))
    
    sample_indices = []
    for label in unique_labels[:n_samples]:
        idx = np.where(labels == label)[0][0]
        sample_indices.append(idx)
    
    # Create figure
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    axes = axes.flatten()
    
    for i, idx in enumerate(sample_indices):
        patch = patches[idx]
        label = labels[idx]
        
        # Create RGB composite (B04-Red, B03-Green, B02-Blue)
        if patch.shape[2] >= 3:
            rgb = patch[:, :, [2, 1, 0]].astype(float)
            
            # Normalize for display
            p2, p98 = np.percentile(rgb, (2, 98))
            rgb = np.clip((rgb - p2) / (p98 - p2), 0, 1)
            
            axes[i].imshow(rgb)
            
            class_name = CORINEProcessor.CORINE_CLASSES.get(label, "Unknown")
            axes[i].set_title(f"Class {label}: {class_name}\n{patch.shape[0]}x{patch.shape[1]} pixels", 
                            fontsize=10)
            axes[i].axis('off')
    
    # Hide unused subplots
    for i in range(len(sample_indices), len(axes)):
        axes[i].axis('off')
    
    plt.suptitle("Sample Patches with CORINE Labels", fontsize=14, fontweight='bold')
    plt.tight_layout()
    
    if output_path:
        plt.savefig(output_path, dpi=150, bbox_inches='tight')
        print(f"\n✓ Visualization saved: {output_path}")
    else:
        plt.show()
    
    plt.close()


# Add this diagnostic function to check CORINE coverage
def diagnose_corine_coverage(corine_path, s2_path, logger):
    """
    Diagnose CORINE coverage over S2 tile
    """
    logger.section("Diagnosing CORINE Coverage")
    
    try:
        # Open both datasets
        s2_ds = gdal.Open(str(s2_path), gdal.GA_ReadOnly)
        corine_ds = gdal.Open(str(corine_path), gdal.GA_ReadOnly)
        
        if s2_ds is None or corine_ds is None:
            logger.error("Could not open files for diagnosis")
            return False
        
        # Get S2 extent
        s2_gt = s2_ds.GetGeoTransform()
        s2_ulx = s2_gt[0]
        s2_uly = s2_gt[3]
        s2_lrx = s2_ulx + s2_ds.RasterXSize * s2_gt[1]
        s2_lry = s2_uly + s2_ds.RasterYSize * s2_gt[5]
        
        logger.info(f"S2 Tile Extent:")
        logger.info(f"  UL: ({s2_ulx:.0f}, {s2_uly:.0f})", indent=1)
        logger.info(f"  LR: ({s2_lrx:.0f}, {s2_lry:.0f})", indent=1)
        
        # Read a sample of CORINE data
        width = min(corine_ds.RasterXSize, 1000)
        height = min(corine_ds.RasterYSize, 1000)
        
        corine_sample = corine_ds.GetRasterBand(1).ReadAsArray(0, 0, width, height)
        unique_values = np.unique(corine_sample)
        
        logger.info(f"\nCORINE Data Sample:")
        logger.info(f"  Unique values: {unique_values[:20]}", indent=1)
        
        # Check for valid CORINE classes (1-44 in raster format)
        valid_corine = unique_values[(unique_values >= 1) & (unique_values <= 44)]
        
        if len(valid_corine) == 0:
            logger.warn("No valid CORINE classes found in sample!")
            logger.warn("This tile may be outside CORINE coverage area", indent=1)
            return False
        
        logger.info(f"  Valid CORINE classes: {valid_corine}", indent=1)
        
        # Read full CORINE aligned data to check
        corine_full = corine_ds.GetRasterBand(1).ReadAsArray()
        unique_full = np.unique(corine_full)
        valid_full = unique_full[(unique_full >= 1) & (unique_full <= 44)]
        
        logger.info(f"\nFull Aligned CORINE:")
        logger.info(f"  Total unique values: {len(unique_full)}", indent=1)
        logger.info(f"  Valid CORINE classes: {len(valid_full)}", indent=1)
        
        if len(valid_full) > 0:
            logger.info(f"  Classes present: {valid_full}", indent=1)
        else:
            logger.error("NO VALID CORINE DATA IN ALIGNED TILE!")
            logger.info("Possible causes:", indent=1)
            logger.info("  1. S2 tile is outside CORINE coverage (e.g., Iceland)", indent=2)
            logger.info("  2. Projection mismatch during alignment", indent=2)
            logger.info("  3. CORINE file is corrupted", indent=2)
            return False
        
        s2_ds = None
        corine_ds = None
        
        return True
        
    except Exception as e:
        logger.error(f"Diagnosis failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Main processing pipeline"""
    
    parser = argparse.ArgumentParser(
        description='Process Sentinel-2 and CORINE data for ML training',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Process a single S2 tile
  python preprocess_corine_s2.py --s2_tile /path/to/S2A_MSIL2A_*.SAFE
  
  # Custom patch size and limit
  python preprocess_corine_s2.py --s2_tile /path/to/*.SAFE --patch_size 5 --max_patches 100000
  
  # With visualization
  python preprocess_corine_s2.py --s2_tile /path/to/*.SAFE --visualize
        """
    )
    
    parser.add_argument('--s2_tile', required=True, help='Path to Sentinel-2 SAFE directory')
    parser.add_argument('--corine', default='/p/scratch/training2600/CORINE/u2018_clc2018_v2020_20u1_raster100m/DATA/U2018_CLC2018_V2020_20u1.tif',
                       help='Path to CORINE GeoTIFF')
    parser.add_argument('--output_dir', default=None, help='Output directory (default: auto-generate)')
    parser.add_argument('--patch_size', type=int, default=3, help='Patch size in pixels (default: 3)')
    parser.add_argument('--stride', type=int, default=None, help='Stride for patch extraction (default: same as patch_size)')
    parser.add_argument('--max_patches', type=int, default=50000, help='Maximum patches to extract (default: 50000)')
    parser.add_argument('--visualize', action='store_true', help='Create visualization of sample patches')
    parser.add_argument('--verbose', action='store_true', help='Verbose output')
    
    args = parser.parse_args()
    
    # Initialize logger
    logger = Logger(verbose=args.verbose or True)
    
    logger.section("Lab 3.2: CORINE & Sentinel-2 Preprocessing")
    print(f"Start time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Setup paths
    s2_safe = Path(args.s2_tile)
    corine_path = Path(args.corine)
    
    if not s2_safe.exists():
        logger.error(f"Sentinel-2 SAFE directory not found: {s2_safe}")
        return 1
    
    if not corine_path.exists():
        logger.error(f"CORINE file not found: {corine_path}")
        return 1
    
    # Setup output directory
    if args.output_dir:
        output_dir = Path(args.output_dir)
    else:
        user = os.environ.get('USER', 'user')
        output_dir = Path(f"/p/scratch/training2600/{user}/training_data")
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    logger.info(f"S2 tile: {s2_safe.name}")
    logger.info(f"CORINE: {corine_path.name}")
    logger.info(f"Output: {output_dir}")
    print()
    
    # Step 1: Process Sentinel-2
    logger.section("Step 1: Processing Sentinel-2 Bands")
    
    s2_processor = Sentinel2Processor(s2_safe, logger)
    band_paths = s2_processor.find_bands()
    
    if not band_paths:
        logger.error("No S2 bands found")
        return 1
    
    s2_stacked = output_dir / f"{s2_safe.stem}_stacked.tif"
    
    if s2_stacked.exists():
        logger.info(f"Stacked S2 file already exists: {s2_stacked.name}")
    else:
        if not s2_processor.stack_bands(band_paths, s2_stacked):
            return 1
    
    # Step 2: Align CORINE
    logger.section("Step 2: Aligning CORINE to Sentinel-2")
    
    corine_processor = CORINEProcessor(corine_path, logger)
    
    if not corine_processor.open():
        return 1
    
    corine_aligned = output_dir / f"corine_aligned_{s2_safe.stem}.tif"
    
    if corine_aligned.exists():
        logger.info(f"Aligned CORINE already exists: {corine_aligned.name}")
    else:
        if not corine_processor.align_to_s2(s2_stacked, corine_aligned):
            return 1
    
    corine_processor.close()

    # In main(), after Step 2 (aligning CORINE), add:

    # Step 2.5: Diagnose CORINE coverage
    if not diagnose_corine_coverage(corine_aligned, s2_stacked, logger):
        logger.section("IMPORTANT: CORINE Coverage Issue Detected")
        logger.warn("This Sentinel-2 tile appears to be outside CORINE coverage.")
        logger.info("CORINE covers EU member states, but NOT Iceland.")
        logger.info("\nOptions:")
        logger.info("  1. Choose a different S2 tile from EU territory", indent=1)
        logger.info("  2. Use alternative land cover data (e.g., ESA WorldCover)", indent=1)
        logger.info("  3. Manually label data for this region", indent=1)
        
        response = input("\nContinue anyway to see the issue? (y/n): ")
        if response.lower() != 'y':
            logger.info("Exiting. Please select a different tile.")
            return 1
    
    # Step 3: Extract patches
    extractor = PatchExtractor(s2_stacked, corine_aligned, logger)
    
    patches, labels, metadata = extractor.extract(
        patch_size=args.patch_size,
        stride=args.stride,
        max_patches=args.max_patches,
        output_dir=output_dir
    )
    
    if patches is None:
        return 1
    
    # Step 4: Visualize (optional)
    if args.visualize and patches is not None:
        logger.section("Creating Visualization")
        
        viz_path = output_dir / f"visualization_{s2_safe.stem}.png"
        visualize_samples(patches, labels, viz_path)
    
    # Summary
    logger.section("Processing Complete!")
    print(f"End time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    logger.info(f"Output directory: {output_dir}")
    logger.info(f"Extracted patches: {len(patches):,}")
    logger.info(f"Unique classes: {metadata['n_classes']}")
    print()
    print("Next steps:")
    print("  1. Review the extracted patches and metadata")
    print("  2. Proceed to Lab 4 for model training")
    print("  3. Use the generated .npz file as training data")
    
    return 0


if __name__ == '__main__':
    sys.exit(main())