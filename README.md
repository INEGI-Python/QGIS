# excel2mapa

## Descripción
`excel2mapa` es un plugin para QGIS que permite importar datos desde archivos Excel y visualizarlos en un mapa. Este plugin facilita la integración de datos tabulares con información geoespacial, permitiendo a los usuarios crear mapas temáticos de manera rápida y eficiente.

## Características
- Importación de datos desde archivos Excel (.xlsx, .xls).
- Asignación de columnas de datos a atributos geoespaciales.
- Creación de capas de puntos, líneas y polígonos a partir de datos tabulares.
- Personalización de estilos y simbología de las capas creadas.
- Soporte para múltiples hojas de cálculo en un solo archivo Excel.

## Requisitos
- QGIS 3.x o superior.
- Python 3.x.
- Librerías adicionales: `pandas`, `openpyxl`.

## Instalación
1. Descargue el archivo del plugin `excel2mapa` desde el repositorio oficial.
2. Abra QGIS y vaya a `Complementos` > `Administrar e instalar complementos`.
3. Haga clic en `Instalar desde ZIP` y seleccione el archivo descargado.
4. Siga las instrucciones en pantalla para completar la instalación.

## Uso
1. Abra QGIS y cargue un proyecto nuevo o existente.
2. Vaya a `Complementos` > `excel2mapa` > `Importar desde Excel`.
3. Seleccione el archivo Excel que desea importar.
4. Asigne las columnas de datos a los atributos geoespaciales correspondientes.
5. Configure las opciones de visualización y haga clic en `Aceptar`.
6. Los datos importados se mostrarán en el mapa como una nueva capa.

## Contribuir
Si desea contribuir al desarrollo de `excel2mapa`, por favor siga estos pasos:
1. Haga un fork del repositorio.
2. Cree una nueva rama para su contribución.
3. Realice los cambios y haga commit.
4. Envíe un pull request describiendo los cambios realizados.

## Licencia
`excel2mapa` está licenciado bajo la Licencia MIT. Consulte el archivo LICENSE para más detalles.

## Contacto
Para preguntas o soporte, por favor contacte a [emmanuel.rodriguez@inegi.org.mx](mailto:emmanuel.rodriguez@inegi.org.mx).
