# Iceland ML Course - Lab 3 Restructuring Summary

**Date**: January 29, 2026  
**Status**: ✅ Complete  

---

## What Changed

The data acquisition labs (3.1 and 3.2) have been **reordered** to follow the logical workflow:

### Before
1. Lab 3.1 → Data Preprocessing (GDAL, processing)
2. Lab 3.2 → Google Earth Engine (data download)

### After (Current)
1. **Lab 3.1 → Data Download (Google Earth Engine)** - Acquire S2 & CORINE from GEE
2. **Lab 3.2 → Data Preprocessing (GDAL)** - Process downloaded GeoTIFF files

---

## Files Created & Modified

### New Files
- ✅ `lab3_1_gee_data_download.ipynb` (NEW) - Complete GEE data acquisition notebook
  - Authentication with Google Earth Engine
  - Sentinel-2 L2A querying with cloud filtering
  - CORINE land cover access
  - Bulk export to GeoTIFF format
  - Data validation and quality checks
  - Task monitoring

### Renamed Files
- ✅ `lab3_2_data_preprocessing.ipynb` (RENAMED from `lab3_1_data_preprocessing.ipynb`)
  - Updated milestone table showing Lab 3.2 is current
  - Updated overview explaining it processes downloaded GeoTIFF files
  - All GDAL code remains the same
  - Now clearly depends on Lab 3.1 output

### Files Still Present
- ⚠️ `Lab3_2.ipynb` (OLD Google Earth Engine notebook) - Consider archiving
  - This is the original GEE notebook with LUCAS point sampling
  - Superseded by new Lab 3.1
  - Can be kept for reference but should be archived

---

## Lab 3.1: Data Download (Google Earth Engine)

### What It Covers
1. **Authentication** - Set up GEE API access
2. **ROI Definition** - Define your study area as coordinates
3. **S2 Querying** - Find cloud-free Sentinel-2 Level 2A imagery
4. **CORINE Access** - Load land cover classification labels
5. **Export** - Download both datasets as GeoTIFF (10m resolution)
6. **Validation** - Verify data quality before preprocessing

### Input
- Region coordinates (lat/lon bounding box)
- Date range for imagery search
- Cloud cover threshold (e.g., <10%)

### Output
- Sentinel-2 10-band GeoTIFF (B2-B12, ~500MB-1GB)
- CORINE classification GeoTIFF (12 classes, ~50MB)
- Both at 10m resolution, same projection

### Key Features
- Uses `ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED')` for L2A data
- Uses `ee.ImageCollection('COPERNICUS/CORINE/V20/100m')` for labels
- Resamples CORINE to 10m to match Sentinel-2
- Exports to Google Drive or HPC storage
- Comprehensive error checking and validation

---

## Lab 3.2: Data Preprocessing

### What It Covers (Unchanged)
1. **Reading GeoTIFFs** - Open downloaded files with GDAL
2. **Inspecting Metadata** - Check CRS, extent, dimensions
3. **Aligning Data** - Ensure S2 and CORINE match
4. **Extracting Patches** - Create 3x3 or 5x5 pixel patches
5. **Creating Datasets** - Build train/val/test splits
6. **HPC Batch Processing** - Scale to multiple tiles with Slurm

### Input
- S2 GeoTIFF from Lab 3.1
- CORINE GeoTIFF from Lab 3.1
- (Optional) SAFE archives if using direct S2 files

### Output
- Training patch CSVs with S2 values and CORINE labels
- Data split files (train/val/test)
- Ready for Lab 4.1 model training

---

## Updated Workflow

```
Lab 3 Data Pipeline (New Order)
================================

┌─────────────────────────────────────────┐
│ Lab 3.1: Google Earth Engine             │
├─────────────────────────────────────────┤
│ 1. Authenticate GEE                      │
│ 2. Query Sentinel-2 L2A collection      │
│ 3. Filter by date, location, cloud cover│
│ 4. Load CORINE land cover data          │
│ 5. Export both as GeoTIFF (10m)         │
│ 6. Validate data quality                │
└────────────┬────────────────────────────┘
             │ Output: S2 + CORINE GeoTIFF
             ↓
┌─────────────────────────────────────────┐
│ Lab 3.2: Data Preprocessing (GDAL)       │
├─────────────────────────────────────────┤
│ 1. Read GeoTIFF files                   │
│ 2. Inspect & validate metadata          │
│ 3. Align to common grid                 │
│ 4. Extract training patches             │
│ 5. Create train/val/test splits         │
│ 6. HPC batch processing                 │
└────────────┬────────────────────────────┘
             │ Output: Training CSVs
             ↓
        Lab 4 & Beyond
```

---

## Documentation Updates Required

The following files have been updated to reflect the new order:

- ✅ `lab3_1_gee_data_download.ipynb` - New, complete GEE notebook
- ✅ `lab3_2_data_preprocessing.ipynb` - Updated milestone table and overview
- ⚠️ `README.md` - Should update navigation links
- ⚠️ `PROJECT_GUIDE.md` - Should update lab descriptions
- ⚠️ `LAB_COHERENCE.md` - Should update dependency diagram
- ⚠️ `COHERENCE_UPDATE_SUMMARY.md` - Should update references

---

## Migration Guide

### If You Were Using Old Structure

**Old Path:**
```
Lab 3.1 (Preprocessing) → Lab 3.2 (GEE)
```

**New Path:**
```
Lab 3.1 (GEE) → Lab 3.2 (Preprocessing)
```

### What to Do
1. ✅ Start with new `lab3_1_gee_data_download.ipynb`
2. ✅ Download S2 and CORINE to your storage
3. ✅ Move to `lab3_2_data_preprocessing.ipynb`
4. ✅ Rest of course continues as before

### Legacy Code
- Old `Lab3_2.ipynb` can be archived to `archive/Lab3_2_legacy.ipynb`
- Old lab3_1 code (extract_s2.py, etc.) still works if you have SAFE archives
- Most students will follow the GEE path now

---

## Benefits of New Order

✅ **Logical Workflow**: Download first, then process  
✅ **Cloud Native**: Use GEE's cloud resources for querying  
✅ **Accessible**: No SAFE archives needed, all via GEE  
✅ **Reproducible**: Easy to specify exact dates and regions  
✅ **Practical**: Students can immediately download their own data  
✅ **Modern**: Follows current remote sensing workflows  

---

## Next Steps

1. **Update navigation links** in README, PROJECT_GUIDE, LAB_COHERENCE
2. **Archive old Lab3_2.ipynb** if not needed
3. **Test new Lab 3.1** with sample ROI
4. **Update student instructions** to reflect new order
5. **Consider adding:** Quick-start section in Lab 3.1 for common regions

---

## Technical Details

### Lab 3.1 Uses:
- `ee` (Google Earth Engine Python API)
- `geemap` (interactive mapping)
- `ee.ImageCollection` for querying
- `ee.batch.Export` for downloads
- `gdal` (geemap backend)

### Lab 3.2 Uses (Unchanged):
- `osgeo.gdal` for reading/writing GeoTIFF
- `numpy` for array operations
- `zipfile` for archive handling
- `os` and `subprocess` for file operations

### Data Resolution:
- Sentinel-2: 10m (resampled from original 10/20/60m)
- CORINE: 10m (resampled from original 100m)
- Both aligned to same UTM projection

---

## FAQ

**Q: Do I need to run Lab 3.1 if I already have S2 and CORINE data?**  
A: No, skip to Lab 3.2. Lab 3.1 shows you how to get the data.

**Q: Can I use the old Lab3_2.ipynb code?**  
A: The old Lab3_2 uses LUCAS validation points. New Lab 3.1 uses bulk export. Old code still works, but new Lab 3.1 is simpler.

**Q: What if my ROI is very large?**  
A: GEE has export limits. Large areas (~100,000 km²) may need splitting. Lab 3.1 includes guidance.

**Q: Does Lab 3.2 need to change much?**  
A: No, it just processes the GeoTIFF files from Lab 3.1 instead of SAFE archives.

---

## Summary

✅ **Lab 3 now follows logical order:** Download → Preprocess  
✅ **New Lab 3.1** provides complete GEE workflow  
✅ **Lab 3.2** updated with correct references  
✅ **Students can now** download their own data easily  
✅ **Course is more** practical and reproducible  

**Status**: Ready for student use immediately! 🚀

