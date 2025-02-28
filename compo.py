from qgis.core import *

def compositor(myCompo):
    proy = QgsProject.instance()
    proyLayMana = proy.layoutManager()
    lay = proyLayMana.layoutByName(myCompo)
    return lay
    
compo = compositor("1:12 000 000")
print(compo)