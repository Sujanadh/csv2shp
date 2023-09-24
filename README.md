# csv2shp

csv2shp is a Python tool for converting CSV data to Shapefile format. It can automatically detect and convert latitude and longitude columns or process WKT geometries in your CSV files.

## Installation

You can install csv2shp package using pip:
pip install csv2shp

### Example

from csv2shp import csv_to_shp

input_file = "path to input csv file"
output_shp = csv_to_shp(input_file)

if you want to save it as a file you can follow steps as;

output_shapefile_path = "path to save output file + .shp"
output_shp.to_file(output_shapefile_path, driver='ESRI Shapefile')

