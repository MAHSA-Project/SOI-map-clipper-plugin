# SOI Map Clipper

A QGIS plugin for detecting and clipping the map area of georeferenced Survey of India (SOI) map sheets.

The plugin was developed as part of the [MAHSA project](https://www.mahsa.arch.cam.ac.uk/) but is not restricted to MAHSA data.

## What does it do?

Georeferenced Survey of India map sheets often contain a border or margin around the actual map area. This can be problematic when using the maps for spatial analysis, as the border and surrounding areas can interfere with analysis or obscure the map content.

SOI Map Clipper automatically detects the map area within a georeferenced raster and clips the raster to this area.

It is designed to work with Survey of India maps at different scales and map extents, including maps covering one or multiple grid squares.

### Input data

The plugin can work with:

- Locally stored GeoTIFF files
- Remote rasters accessible through QGIS, including Cloud Optimized GeoTIFFs (COGs)
- Rasters accessed through STAC-based data infrastructure

This means it can be used either to process maps that have just been georeferenced and saved locally, or to process already georeferenced maps stored remotely.

## Features

- Automatically detects the map area of Survey of India map sheets
- Clips the raster to the detected map area
- Supports different SOI map scales, including 1 inch to 1 mile and 1 inch to 2 miles
- Supports maps covering different numbers of grid squares
- Works with local GeoTIFF files
- Works with remote rasters, including COGs accessed through STAC
- Automatic settings that assess map complexity and select appropriate border-detection parameters
- Automatic line-quality assessment
- Option to mask areas outside the detected map area rather than simply cropping the raster
- User-defined NoData value
- User-defined output data type
- User-defined output CRS
- Option to load the clipped raster automatically after processing
- Option to save the output as a temporary or permanent file
- Debugging options for investigating problems with individual maps

## Requirements

- QGIS 3.40 or later is recommended.
- The plugin has been tested on:
  - QGIS 3.40
  - QGIS 3.44

The plugin was specifically tested on QGIS 3.44 because of the significant changes introduced in this version.

Earlier QGIS versions may work but have not been tested with the current version of the plugin.

## Installation

The plugin is currently distributed as a ZIP file rather than through the QGIS Plugin Repository.

To install the plugin:

1. Download the plugin ZIP file from this repository.
2. Open QGIS.
3. Go to **Plugins → Manage and Install Plugins**.
4. Select **Install from ZIP**.
5. Select the downloaded plugin ZIP file.
6. Follow the installation prompts.

The plugin can then be accessed through the QGIS Processing Toolbox.

## Usage

The plugin is available through the QGIS Processing framework.

Add a georeferenced Survey of India map as a raster layer in QGIS, then run the **SOI Map Clipper** processing tool.

The plugin analyses the raster to identify the lines defining the map area and uses these to determine the area to retain.

The resulting raster can either be saved permanently or created as a temporary output. The user can also choose whether the resulting clipped raster should automatically be loaded into QGIS.

## Survey of India maps

The plugin has been developed and tested specifically with georeferenced Survey of India map sheets. It has been designed to accommodate different SOI map scales and map extents.

The plugin may work with other types of historical maps containing similar map-border characteristics, but this has not been systematically tested.

## Development

This plugin was developed for work with Survey of India maps as part of the [MAHSA project](https://www.mahsa.arch.cam.ac.uk/).

The source code is available in this repository.

## Version history

### 0.6

- Added support for remote rasters, including COGs and rasters accessed through STAC.
- Added debugging options for investigating key parts of the processing workflow.
- Improved the automatic line-quality checker.
- Line-quality thresholds are now dynamically calculated from image pixel statistics rather than using a fixed set of values.
- Added an option to prevent the clipped map from being automatically loaded after processing.

### 0.52

- Bug fixes.
- Added temporary short file names for long TIFF paths.
- Updated values used for automatic line detection.

### 0.51

- Updated to work with QGIS 3.44.

### 0.5

- Added automatic detail assessment.
- The plugin automatically assesses map complexity and selects appropriate settings for searching for border lines.

### 0.4

- Improved handling of maps drawn to incorrect coordinates.
- If a vertical line cannot be found, the plugin changes the search area.

### 0.3

- Added option to mask the area outside the map rather than simply clipping the map.
- Added user selection of NoData value.
- Added user selection of output data type.
- Added user selection of output CRS.

### 0.2

- Updated to use the native CRS of the input raster.
- Added scale settings based on input map size.

### 0.1

- Initial version.

## Issues and feedback

If you encounter a problem with a particular map, please report it through the GitHub issue tracker and, where possible, include information about:

- The SOI map sheet and scale
- QGIS version
- Whether the raster is local or remote
- The processing settings used
- Any error messages or debugging information

## Licence

Licence information to be added.