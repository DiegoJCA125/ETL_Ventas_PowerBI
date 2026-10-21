
import random
from pathlib import Path
from datetime import datetime, timedelta

import pandas as pd

# Fijamos la semilla para generar los mismos datos en cada ejecucion
random.seed(42)

# Definimos las carpetas del proyecto
CARPETA_PROYECTO = Path(__file__).resolve().parent
CARPETA_RAW = CARPETA_PROYECTO / "data" / "raw"
CARPETA_RAW.mkdir(parents=True, exist_ok=True)

# Datos ficticios de la tienda
productos = {
    "Portatil": ("Tecnologia", 2500000),
    "Mouse": ("Tecnologia", 60000),
    "Escritorio": ("Hogar", 450000),
    "Silla": ("Hogar", 320000),
    "Camiseta": ("Ropa", 50000),
    "Zapatos": ("Ropa", 180000),
}

ciudades = ["Armenia", "Pereira", "Manizales", "Cali", "Bogota"]

ventas = []
fecha_inicial = datetime(2026, 1, 1)

# Generamos 500 ventas ficticias
for numero in range(1, 501):
    producto = random.choice(list(productos.keys()))
    categoria, precio = productos[producto]

    fecha = fecha_inicial + timedelta(
        days=random.randint(0, 179)
    )

    ventas.append({
        "id_venta": numero,
        "fecha": fecha.strftime("%Y-%m-%d"),
        "ciudad": random.choice(ciudades),
        "producto": producto,
        "categoria": categoria,
        "precio_unitario": precio,
        "cantidad": random.randint(1, 5),
    })

df = pd.DataFrame(ventas)

# Introducimos errores controlados para probar el ETL
df.loc[10, "ciudad"] = None
df.loc[20, "precio_unitario"] = -100
df.loc[30, "cantidad"] = -2
df.loc[40, "fecha"] = "fecha_invalida"

# Duplicamos una venta para comprobar la deteccion de duplicados
df = pd.concat([df, df.iloc[[0]]], ignore_index=True)

# Guardamos los datos originales sin limpiar
ruta_salida = CARPETA_RAW / "ventas.csv"
df.to_csv(ruta_salida, index=False, encoding="utf-8-sig")

print(f"Archivo generado: {ruta_salida}")
print(f"Registros generados: {len(df)}")
