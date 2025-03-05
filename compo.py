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




def leeXML():
	import xml.etree.ElementTree as ET
	import pandas as pd
	import os
	if os.path.exists("excel2mapa/plantilla/ultima/MapasInegi2025_V1.xml"):
		tree = ET.parse("excel2mapa/plantilla/ultima/MapasInegi2025_V1.xml")
		root = tree.getroot()
		datos = []
		for child in root:
			print(child.attrib)
			#datos.append([child.attrib["colorramp"],child.attrib["columna"],child.attrib["tipo"],child.attrib["color"],child.attrib["simbolo"]])
		    #return pd.DataFrame(datos,columns=["colorramp","Columna","Tipo","Color","Simbolo"])
	else:
		return pd.DataFrame(columns=["colorramp","Columna","Tipo","Color","Simbolo"])