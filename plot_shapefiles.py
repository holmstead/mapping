import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
from geopy.distance import geodesic

## IRELAND
#shp = "~/geospatial_files/ireland/IRL_adm/IRL_adm0.shp"
shp = "~/geospatial_files/ireland/IRL_adm/IRL_adm1.shp"
#shp = "~/geospatial_files/ireland/IRL_01/ie_1km.shp"

## ire aquaculture 
aqua_shp = "~/geospatial_files/ireland/Aquaculture_1/Aquaculture_1.shp"

roads_shp = "~/geospatial_files/ireland/NationalRoads2013/NationalRoads2013.shp"
rivers_json = "~/geospatial_files/ireland/WATER_RIVNETROUTES.json"

## ITALY
#shp = "~/geospatial_files/italy/italy-waterways-shape/waterways.shp"
#shp = "~/geospatial_files/italy/italy-natural-shape/natural.shp"
#shp = "~/geospatial_files/italy/italy-roads-shape/roads.shp"
#shp = "~/geospatial_files/italy/italy-places-shape/places.shp"
#shp = "~/geospatial_files/italy/italy-points-shape/points.shp"
#shp = "~/geospatial_files/italy/italy-railways-shape/railways.shp"
#shp = "~/geospatial_files/italy/italy-building-shape/building.shp"
#shp = "~/geospatial_files/italy/Italy_shapefile/it_1km.shp"


# read in shapefiles
shape_01 = gpd.read_file(shp)
shape_02 = gpd.read_file(roads_shp)
#shape_03 = gpd.read_file(rivers_shp)

print(shape_01)

# read in csv dataset using pandas and create a dataframe
hospitals = "~/ire_hospitals.txt"
df = pd.read_csv(hospitals)
#print(df, '\n')

# use geopandas to convert "lat" and "lon" in the dataframe to points
# this gives us a new "geodataframe"
df_geo = gpd.GeoDataFrame(df, geometry = gpd.points_from_xy(df.lon, df.lat))
#print(df_geo, '\n')

# to begin plotting the data, first create an axis
ax = shape_01.plot()

# plot the first shapefile using this "ax"
#shape_01.plot(ax=ax, color = 'green', facecolor="none", edgecolor="black", linewidth=0.05)#, legend=True

# plot the second shapefile
#shape_02.plot(ax=ax, color = 'black', facecolor="none", zorder=1)#, edgecolor="blue",#, legend=True

# read in geojson data
#geojson_planning = gpd.read_file("/home/holmstead/datasets/geospatial_files/ireland/IrishPlanningApplications.geojson")
geojson_rivers = gpd.read_file(rivers_json)
geojson_rivers.plot(ax=ax, color = 'red', facecolor="none", zorder=2)#, edgecolor="blue",#, legend=True


# plot the hospital data
#df_geo.plot(ax = ax, color = 'black', legend=True, facecolor="blue", edgecolor="blue")

# now to calculate the heatmap for distance from a hospital
# define the points of interest (latitude and longitude)
# Iterate over the rows of the DataFrame
#hosp = (52.663362, -8.616857)


# calculate the distance from the point for each location in the shapefile
#distances = []
#for index, row in shape_01.iterrows():
    #location = (row[9])
    #print(location)
    #distance = geodesic(hosp, location).km
    #distances.append(distance)

# add the distance data to the shapefile
#shp['distance'] = distances

# plot the shapefile and distance data as a heatmap
#shp.plot(column='distance', cmap='viridis', ax=ax)





# save the figure
plt.savefig("IRL_adm1_roads.png", dpi=500, bbox_inches='tight')

# display the figure
plt.show()

