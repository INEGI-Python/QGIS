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



def composicionMapa():
	from  qgis.core import QgsProject,QgsVectorLayer,QgsVectorFileWriter,QgsApplication,QgsLayout,QgsLayoutItemMap,QgsLayoutItemLegend,QgsLayoutItemLabel,QgsLayoutItemScaleBar,QgsLayoutItemAttributeTable
	from qgis.gui import QgsExpressionContextUtils
	import os		
	app = QgsApplication([], False)
	app.initQgis()	
	project = QgsProject.instance()
	project.read("excel2mapa/plantilla/ultima/MapasInegi2025_V1.qgs")	
	capas = ["estados","municipios","localidades","secciones"]
	




def leeXML():
	import xml.etree.ElementTree as ET
	import pandas as pd
	import os,json
	jsonRampa={"colorramps":[]}
	if os.path.exists("excel2mapa/plantilla/ultima/MapasInegi2025_V1.xml"):
		tree = ET.parse("excel2mapa/plantilla/ultima/MapasInegi2025_V1.xml")
		rampas = tree.findall(".//colorramp")
		for rampa in rampas:
			jsonRampa["colorramps"].append({"name":rampa.attrib["name"],"type":rampa.attrib["type"],"colors":[ c.attrib["value"] for c in rampa.iter() if c.attrib["type"]=="QString"]})
		arch = open("excel2mapa/plantilla/estilos-INEGI.json","w",encoding="utf-8")
		arch.write(json.dumps(jsonRampa,indent=4))
		arch.close()	
leeXML()





"""['__bool__', '__class__', '__copy__', '__deepcopy__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', 
'__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', 
'__init_subclass__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
 '__repr__', '__setattr__', '__setitem__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'attrib', 
 'clear', 'extend', 'find', 'findall', 'findtext', 'get', 'insert', 'items', 'iter', 'iterfind', 'itertext', 'keys', 'makeelement', 'remove', 
 'set', 'tag', 'tail', 'text']   """