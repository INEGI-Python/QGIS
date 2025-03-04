def unirDatos(capa,excel):
	import geopandas as geo
	import os
	
	if os.path.exists(f"excel2mapa/plantilla/{capa}_composicion.shp"):
		os.remove(f"excel2mapa/plantilla/{capa}_composicion.shp")
	
	datos = geo.read_file("excel2mapa/plantilla/TemplateQgis_3_34.gpkg",layer=f"{capa}_finales",columns=['CVEGEO','CVE_ENT','CVE_MUN','NOMGEO','geometry'],encoding='utf-8') 
	datos["CVEGEO"] = datos["CVEGEO"].astype('Int64')
	datos.set_index('CVEGEO',inplace=True)
	union = datos.join(excel)
	union.sort_values("Clase")
	union.to_file(f"excel2mapa/plantilla/{capa}_composicion.shp", index=True)