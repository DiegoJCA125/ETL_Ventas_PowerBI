📊 ETL de Ventas y Dashboard en Power BI

Proyecto de portafolio de Ingeniería de Datos que simula ventas comerciales y transforma datos sin procesar en información útil para el análisis del negocio.

🎯 Objetivo

Construir un pipeline ETL con Python para limpiar, validar y transformar datos de ventas, y visualizarlos en un dashboard interactivo desarrollado en Power BI.

🛠️ Tecnologías utilizadas

Python: generación y procesamiento de datos.

Pandas: limpieza, transformación y validación.

Power BI: visualización y análisis interactivo.

DAX: creación de medidas e indicadores.

Git y GitHub: control de versiones y publicación del proyecto.

unittest: pruebas automatizadas de las transformaciones.

🔄 Flujo del proyecto

Extracción: lectura de un archivo CSV con ventas ficticias.

Transformación: eliminación de duplicados, manejo de datos faltantes y fechas inválidas, y validación de precios y cantidades.

Cálculo: generación del valor total de cada venta.

Carga: exportación de los datos limpios a un nuevo archivo CSV.

Visualización: conexión del archivo procesado con Power BI para construir un dashboard interactivo.

📈 Dashboard de ventas

El informe permite analizar el comportamiento comercial mediante:

Ventas totales.

Número de ventas.

Unidades vendidas.

Ticket promedio.

Ventas por mes.

Ventas por producto.

Filtros interactivos por ciudad, categoría y fecha.

🧹 Calidad de datos

El pipeline contempla reglas para:

Detectar y eliminar ventas duplicadas por identificador.

Excluir registros con información obligatoria faltante.

Convertir fechas y valores numéricos a sus tipos correctos.

Descartar precios y cantidades inválidos.

Calcular los ingresos de cada transacción.

Se incluyen pruebas automatizadas para comprobar la eliminación de duplicados, el cálculo del total de venta y el rechazo de precios negativos.

📁 Estructura del repositorio

ETL_Ventas_PowerBI/
├── data/
│   ├── raw/
│   │   └── ventas.csv
│   └── processed/
│       └── ventas_limpias.csv
├── etl/
│   ├── __init__.py
│   └── pipeline.py
├── tests/
│   └── test_pipeline.py
├── dashboard/
│   └── ventas_powerbi.pbix
├── generar_datos.py
├── requirements.txt
├── .gitignore
└── README.md

⚙️ Cómo ejecutar el proyecto

1. Clonar el repositorio

git clone URL_DE_TU_REPOSITORIO
cd ETL_Ventas_PowerBI

2. Crear y activar un entorno virtual

En Windows:

python -m venv .venv
.\.venv\Scripts\Activate.ps1

3. Instalar las dependencias

python -m pip install -r requirements.txt

4. Generar los datos de prueba

python generar_datos.py

5. Ejecutar el pipeline ETL

python -m etl.pipeline

6. Ejecutar las pruebas automatizadas

python -m unittest discover -s tests -v

7. Abrir el dashboard

Abrir dashboard/ventas_powerbi.pbix con Power BI Desktop.

📌 Resultados esperados

Archivo CSV original con ventas ficticias.

Archivo CSV procesado y listo para análisis.

Pruebas automatizadas de reglas básicas de calidad.

Dashboard interactivo para explorar indicadores comerciales.

🔐 Datos

Todos los datos son sintéticos y se utilizan exclusivamente con fines educativos. El proyecto no contiene información real de clientes ni de empresas.

👨‍💻 Autor

Proyecto desarrollado como parte de mi aprendizaje práctico en Ingeniería de Datos, con enfoque en procesamiento de datos, calidad, SQL analítico y visualización de información.