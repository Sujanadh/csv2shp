import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
from shapely import wkt

def csv_to_shp(input_csv):
    # Read the CSV data
    csv_data = pd.read_csv(input_csv)

    lat_col, lon_col = None, None

    for col in csv_data.columns:
        if pd.api.types.is_numeric_dtype(csv_data[col]):
            if lat_col is None:
                lat_col = col
            elif lon_col is None:
                lon_col = col
                break

    if lat_col is not None and lon_col is not None:
        # Create Point geometries from latitude and longitude columns
        csv_data['geometry'] = [Point(lon, lat) for lat, lon in zip(csv_data[lat_col], csv_data[lon_col])]
    elif 'Geometry' in csv_data.columns:
        csv_data['Geometry'] = csv_data['Geometry'].astype(str)

        # Remove SRID prefix and convert to Shapely geometry
        csv_data['geometry'] = csv_data['Geometry'].str.replace(r'SRID=\d+;', '', regex=True)

        # Handle NaN values in the 'geometry' column
        csv_data['geometry'] = csv_data['geometry'].apply(handle_nan_in_geometry)

        # Remove rows with invalid geometries (e.g., 'NaN' or non-POLYGON geometries)
        csv_data = csv_data.dropna(subset=['geometry'])
        csv_data = csv_data[csv_data['geometry'].apply(lambda geom: geom.geom_type == 'Polygon')]

    else:
        raise ValueError("The CSV does not contain valid latitude and longitude columns or a 'Geometry' column.")

    # Create a GeoDataFrame
    gdf = gpd.GeoDataFrame(csv_data, geometry='geometry', crs="EPSG:4326")

    return gdf

def handle_nan_in_geometry(geometry_str):
    if geometry_str.lower() == 'nan':
        return None
    try:
        return wkt.loads(geometry_str)
    except Exception as e:
        print(f"Error parsing WKT: {e}")
        return None

