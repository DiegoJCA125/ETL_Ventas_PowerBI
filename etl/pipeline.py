
from pathlib import Path

import pandas as pd

# Encontramos la raíz del proyecto sin depender de la carpeta
# desde la que se ejecute el comando
RAIZ = Path(__file__).resolve().parent.parent

ARCHIVO_RAW = RAIZ / "data" / "raw" / "ventas.csv"
ARCHIVO_PROCESADO = (
    RAIZ / "data" / "processed" / "ventas_limpias.csv"
)


def extraer():
    """Lee el archivo original de ventas."""
    if not ARCHIVO_RAW.exists():
        raise FileNotFoundError(
            f"No se encontró el archivo: {ARCHIVO_RAW}"
        )

    # Leemos el CSV con Pandas
    return pd.read_csv(ARCHIVO_RAW)


def transformar(df):
    """Limpia los datos y calcula el valor de cada venta."""

    # Trabajamos sobre una copia para no modificar el original
    df = df.copy()

    filas_iniciales = len(df)

    # Eliminamos ventas duplicadas según su identificador
    df = df.drop_duplicates(subset="id_venta", keep="first")

    # Convertimos las columnas a sus tipos correctos
    df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce")
    df["precio_unitario"] = pd.to_numeric(
        df["precio_unitario"], errors="coerce"
    )
    df["cantidad"] = pd.to_numeric(
        df["cantidad"], errors="coerce"
    )

    # Eliminamos filas con información esencial faltante
    columnas_obligatorias = [
        "id_venta", "fecha", "ciudad", "producto",
        "categoria", "precio_unitario", "cantidad"
    ]
    df = df.dropna(subset=columnas_obligatorias)

    # Eliminamos precios y cantidades que no tengan sentido
    df = df[
        (df["precio_unitario"] > 0)
        & (df["cantidad"] > 0)
    ]

    # Convertimos cantidades a enteros si son números enteros
    df = df[df["cantidad"] % 1 == 0].copy()
    df["cantidad"] = df["cantidad"].astype(int)

    # Calculamos el ingreso generado por cada venta
    df["total_venta"] = (
        df["precio_unitario"] * df["cantidad"]
    )

    # Creamos columnas útiles para los análisis de Power BI
    df["anio"] = df["fecha"].dt.year
    df["mes"] = df["fecha"].dt.month
    df["nombre_mes"] = df["fecha"].dt.strftime("%B")

    # Devolvemos los registros válidos con un índice limpio
    df = df.reset_index(drop=True)

    print(f"Filas iniciales: {filas_iniciales}")
    print(f"Filas válidas: {len(df)}")
    print(f"Filas descartadas: {filas_iniciales - len(df)}")

    return df


def cargar(df):
    """Guarda los datos limpios para utilizarlos en Power BI."""

    # Creamos la carpeta de destino si todavía no existe
    ARCHIVO_PROCESADO.parent.mkdir(
        parents=True, exist_ok=True
    )

    # Exportamos el archivo sin la columna de índices
    df.to_csv(
        ARCHIVO_PROCESADO,
        index=False,
        encoding="utf-8-sig"
    )

    print(f"Archivo procesado guardado en: {ARCHIVO_PROCESADO}")


def ejecutar_pipeline():
    """Ejecuta el proceso ETL completo."""

    print("=== INICIANDO PIPELINE ETL ===")

    # E: extraer los datos originales
    datos = extraer()

    # T: limpiar y transformar
    datos_limpios = transformar(datos)

    # L: cargar los datos preparados
    cargar(datos_limpios)

    print("=== PIPELINE FINALIZADO ===")


# Solo ejecutamos el pipeline al ejecutar directamente este archivo
if __name__ == "__main__":
    ejecutar_pipeline()
