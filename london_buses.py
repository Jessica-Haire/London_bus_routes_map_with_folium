import matplotlib.pyplot as plt
import geopandas as gpd
import contextily as cx
import shapely
from shapely.geometry import Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygon

buses_gdf = gpd.read_file("C:\\Users\\0zn1z\Desktop\Data Sets\\PythonProjects\\busroutes.shp")
#print(buses_gdf.crs)
# #print(buses_gdf.head())

# ax = buses_gdf.plot(
#     color='white', edgecolor='black')
# buses_gdf.plot(ax=ax, color='red')

buses_gdf_wm = buses_gdf.to_crs('EPSG:4326')

ax = buses_gdf_wm.plot(figsize=(20, 20), alpha=0.5, edgecolor='k')
cx.add_basemap(ax, crs=buses_gdf_wm.crs.to_string())
plt.show()







