import ee
import geemap
import pyproj
import pandas as pd
import matplotlib.pyplot as plt

from tqdm.auto import tqdm

country_geometry = r"D:\All Python\Pure-Python\P2\12-Work-GITI\06-Earth_Engine\countries_geometry.csv"
my_geometry = r"D:\All Python\Pure-Python\P2\12-Work-GITI\06-Earth_Engine\my_geometry.csv"

class Map_functions:
    def __init__(self):
        pass

    def add_nvdi(self, img):
        ndvi = img.normalizedDifference(["B8", "B4"]).rename("ndvi")
        return img.addBands(ndvi)

class GEE_Toolkit(Map_functions):
    def __init__(self):
        super().__init__()
        # ee.Authenticate()
        # ee.Initialize()
        self.map = geemap.Map()
        self.map.addLayerControl()
        self.map.add_draw_control()
        self.all_countries_geometry = pd.read_csv(country_geometry)
        self.my_geometry = pd.read_csv(my_geometry)
        self.features_list = ["slope", "aspect", "hillshade"]
        self.last_selected_location = None

    def get_drawn_info(self):
        # Retrieve the drawn features
        drawn_features = self.map.draw_last_feature
        if drawn_features:
            # Extract the geometry of the drawn feature
            geom = drawn_features.geometry()
            coords = geom.coordinates().getInfo()
            print("[INFO] Drawn feature coordinates:", coords)
            self.last_selected_location = geom
            return geom
        else:
            print("[ERROR] No feature drawn yet.")

    def set_map(self, centered_obj, zoom=12):
        self.map.center_object(ee_object=centered_obj, zoom=zoom)

    def get_image(self, image_name:str):
        return ee.Image(image_name)
    
    def get_imagecollection(self, collection_name:str):
        return ee.ImageCollection(collection_name)
    
    def get_terrain_features(self, feature:str, data):
        if feature in self.features_list:
            if feature == "slope":
                return ee.Terrain.slope(data)
            elif feature == "aspect":
                return ee.Terrain.aspect(data)
            elif feature == "hillshade":
                return ee.Terrain.hillshade(data)
        else:
            print(f"[ERROR] {feature} not exists!")
    
    def add_layer(self, layer, vis_params:dict={}, name:str=None, shown: bool=True, opacity:float=1.0) -> None:
        self.map.addLayer(ee_object=layer, 
                          vis_params=vis_params,
                          name=name,
                          shown=shown,
                          opacity=opacity)
        
    def vis_params_maker(self, bands = None, min_: float = None, max_: float = None, palette: list = None) -> dict:
        vis_param = {}
        if bands is not None:
            vis_param["bands"] = bands
        if min_ is not None:
            vis_param["min"] = min_
        if max_ is not None:
            vis_param["max"] = max_
        if palette is not None:
            vis_param["palette"] = palette
        return vis_param
    
    def get_geometry(self, country:str=None, place:str=None):
        if country and not place:
            data = self.all_countries_geometry
            name = "Country"
            location = country
        elif place and not country:
            data = self.my_geometry
            name = "Place"
            location = place
        else:
            print(f"[ERROR] You should only put one of the country or place. Not both at the same time.")
            return None

        location_list = list(data[name])
        if location == "All":
            print(location_list)
        elif location in location_list:
            objective_geo = data[data[name]==location].iloc[0]
            coords = objective_geo[1:].apply(lambda x: list(map(float, x[1:-1].split(", "))) if isinstance(x, str) else None).dropna().tolist()
            # Explanation:
            # coords = []
            # for i in objective_geo[1:]:
            #     if type(i) == str:
            #         temp = i[1:-1].split(", ")
            #         temp = [float(i) for i in temp]
            #         coords.append(temp)
            req_geometry = ee.Geometry.Polygon([coords])
            return req_geometry
        else:
            print(f"[INFO] There is no country with the name of {location}!!! Set location to 'ALL' to see all.")

    def reduce_to_one(self, property, reducer, geometry, scale):
        if reducer == "mean":
            reducer_temp = ee.Reducer.mean()
        elif reducer == "sum":
            reducer_temp = ee.Reducer.sum()

        result = property.reduceRegion(reducer=reducer_temp,
                                       geometry=geometry,
                                       scale=scale)
        return result
    
    def to_latlon(self, utm_zone, utm_x, utm_y, northern_hemisphere):
        proj_utm = pyproj.Proj(proj='utm', zone=utm_zone, datum='WGS84', south=not northern_hemisphere)
        proj_latlon = pyproj.Proj(proj='latlong', datum='WGS84')

        longitude, latitude = pyproj.transform(proj_utm, proj_latlon, utm_x, utm_y)
        return longitude, latitude
    
    def get_bands_name(self, collection):
        print(collection.first().bandNames().getInfo())

    def extract_time_series(self, collection, geometry, bands, reducer='mean', scale=30):
        def get_date_values(img):
            img = self.add_nvdi(img)
            date = ee.Date(img.get("system:time_start")).format("YYYY-MM-dd").getInfo()
            value = img.select(bands).reduceRegion(reducer=ee.Reducer.mean(),
                                                        geometry=geometry,
                                                        scale=scale).getInfo()
            return date, value
        
        collection_list = collection.toList(collection.size()).getInfo()
        collection_data = []
        for img_info_i in tqdm(range(len(collection_list))):
            img = ee.Image(collection_list[img_info_i]["id"])
            date, value = get_date_values(img)
            collection_data.append({"Date": date})
            for key in bands:
                collection_data[-1][key] = value[key]
        return collection_data
    
    def plot_time_series(self, features, title='Time Series', ylabel='Value'):
        data = pd.DataFrame(features)
        data["Date"] = pd.to_datetime(data["Date"])
        data.set_index("Date", inplace=True)
        data.sort_values(by="Date", inplace=True)
        data.dropna(inplace=True)
        plt.figure(figsize=(10, 5))
        data.plot()
        plt.xlabel('Date')
        plt.ylabel(ylabel)
        plt.title(title)
        plt.grid(True)
        plt.show()



