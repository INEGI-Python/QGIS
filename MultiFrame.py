import pandas as  pan 
proyect = QgsProject.instance()
proxe = proyect.layoutManager()
layout = proxe.layoutByName("Escala 1:31 000 000 Tabla")
marco = [i for i in layout.items() if isinstance(i,QgsLayoutFrame)][0]
print(marco.id())
multiMarco = marco.multiFrame()
Tabla = multiMarco.tableContents()
file="D:/misDocs/2025/INEGI/QGIS/Población LGBT+ (ENDISEG) 2021.xlsx"
aux = pan.read_excel(file,index_col=None,header=0,sheet_name="Datos")
datosTabla=None
if "Tabla" in aux.columns:
    datosTabla=aux.loc[:,["CVEGEO","Tabla"]]
    datosTabla.sort_values(by="CVEGEO",inplace=True)
for i in range(1,33):
    new_cell = QgsTableCell(f"   - {str(datosTabla.loc[i-1,"Tabla"])} -")
    txt_format = QgsTextFormat()
    txt_format.setFont(QFont('Times'))
    txt_format.setSize(8)
    txt_format.setColor(QColor(0, 0, 0))
    new_cell.setTextFormat(txt_format)
    Tabla[i if i< 17 else i-16][1 if i<17 else 3]=new_cell
multiMarco.setTableContents(Tabla)
layout.refresh()
layout.update()

