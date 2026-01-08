# Lab 3 — Sentinel-2 Acquisition (GEE) (2 hours)

**Notebook:** [notebooks/iceland-ml/lab3_gee_sentinel2_acquisition.ipynb](../../notebooks/iceland-ml/lab3_gee_sentinel2_acquisition.ipynb)

## ⏱️ Time Allocation (2 hours)
- **10 min:** Introduction to Google Earth Engine
- **20 min:** GEE authentication and setup
- **30 min:** AOI definition and image collection query
- **25 min:** Scene filtering and visualization
- **25 min:** Export and download workflow
- **10 min:** Advanced filtering (optional) + Q&A

## Goals
### Core (Essential)
- Authenticate with Google Earth Engine
- Define an AOI in Iceland (Þingvellir region)
- Filter Sentinel-2 scenes by cloud cover (<20%)
- Visualize scenes (RGB and false color composites)
- Export/download four scenes for downstream processing

### Optional (Time Permitting)
- Multiple AOI comparison
- Temporal analysis (seasonal changes)
- Advanced cloud masking with QA bands
- Custom band combinations (NDVI, NDWI, NBR)
- Batch export for larger datasets

## Outputs
### Required
- Four GeoTIFF scenes with metadata
- AOI definition saved for reuse
- Notes on acquisition dates and cloud cover

### Bonus
- Additional spectral indices calculated
- Time series visualization
- Cloud mask quality assessment
- Bulk export configuration

## 📚 Session Structure

### Part 1: GEE Setup (30 min)
1. **Introduction to GEE** (10 min)
   - What is Google Earth Engine?
   - Server-side vs client-side processing
   - Data catalog overview
   - Sentinel-2 in GEE
   - **Demo:** GEE Code Editor tour

2. **Authentication** (20 min)
   - GEE account verification
   - Python API authentication
   - Token management
   - **Troubleshooting:** Common auth issues
   - **Exercise:** Verify access to catalog

### Part 2: Data Discovery (55 min)
3. **AOI Definition** (15 min)
   - Why Þingvellir, Iceland?
   - Define bounding box or polygon
   - Visualize AOI on map
   - Load from GeoJSON/shapefile
   - **Exercise:** Create custom AOI

4. **Image Collection Query** (20 min)
   - Filter by date range
   - Filter by bounds (AOI)
   - Filter by cloud cover percentage
   - Collection size and statistics
   - **Demo:** Query optimization

5. **Scene Visualization** (20 min)
   - True color RGB (B4, B3, B2)
   - False color composites (B8, B4, B3)
   - SWIR composites for geology
   - Adjust visualization parameters
   - **Exercise:** Compare different date ranges

### Part 3: Export and Download (35 min)
6. **Export Workflow** (15 min)
   - Export to Google Drive
   - Export to Cloud Storage
   - GEE export limits and quotas
   - File formats (GeoTIFF recommended)
   - **Demo:** Submit export task

7. **Download and Verification** (20 min)
   - Download from Drive
   - Verify with rasterio/GDAL
   - Check band count, resolution, CRS
   - Metadata inspection
   - **Exercise:** Validate all four scenes

### Part 4: Advanced Topics (Optional, 10+ min)
8. **Advanced Filtering** (if time permits)
   - Custom cloud masking with QA60 band
   - Temporal compositing (median, mean)
   - Calculate spectral indices:
     - NDVI: (NIR - Red) / (NIR + Red)
     - NDWI: (Green - NIR) / (Green + NIR)
     - NBR: (NIR - SWIR) / (NIR + SWIR)
   - **Exercise:** Create NDVI layer

9. **Q&A and Next Steps** (5 min)

## 🎯 If You Finish Early
- **Expanded Analysis:**
  - Compare multiple AOIs (different landscapes)
  - Seasonal time series (winter vs summer)
  - Cloud-free mosaic creation
  - Export higher-resolution PlanetScope or Maxar data (if available)

- **Spectral Indices:**
  - Calculate and visualize NDVI for vegetation
  - NDWI for water bodies
  - NBR for burn severity
  - Custom indices for your project

- **Advanced GEE:**
  - Write functions and map over collections
  - Reducers for statistics
  - Chart generation (time series plots)
  - GEE Apps for interactive exploration

- **Data Alternatives:**
  - Explore Landsat 8/9 data
  - Compare with Sentinel-1 SAR
  - Access MODIS for larger-scale analysis

## ✂️ If Running Out of Time
**Priority 1 (Must Complete - 75 min):**
- GEE authentication (15 min)
- AOI definition (10 min)
- Query and filter collection (15 min)
- Export four scenes (20 min)
- Download and verify (15 min)

**Can Skip:**
- Detailed visualization exploration (provide examples)
- False color composites (focus on RGB only)
- Advanced cloud masking (use default)
- Spectral indices

**Can Use Pre-downloaded Data:**
- If GEE auth issues persist (>20 min), provide backup scenes
- Students can explore GEE later asynchronously

**Minimal Viable Lab (90 min):**
- Quick GEE setup (10 min)
- Use provided AOI (5 min saved)
- Basic query with cloud filter (15 min)
- Export 2 scenes instead of 4 (15 min saved)
- Download one scene to verify (10 min)
- Provide other scenes pre-downloaded

**Backup Plan:**
- If GEE accounts not approved: Use pre-downloaded scenes
- Focus on understanding GEE concepts via demo
- Students apply for accounts during lab (for future use)
