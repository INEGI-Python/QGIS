import geopandas as geo

datos = geo.read_file("mun.shp",columns=['CVEGEO','CVE_ENT','CVE_MUN','NOMGEO','geometry'])
datos.set_index('CVEGEO',inplace=True)
datos.to_file("excel2mapa/plantilla/municipios_2024.shp", index=True)
