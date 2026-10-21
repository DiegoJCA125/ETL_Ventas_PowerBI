
import unittest
import pandas as pd

from etl.pipeline import transformar


class PruebasPipeline(unittest.TestCase):

    def test_elimina_duplicados(self):
        datos = pd.DataFrame([
            {
                "id_venta": 1,
                "fecha": "2026-01-10",
                "ciudad": "Armenia",
                "producto": "Mouse",
                "categoria": "Tecnologia",
                "precio_unitario": 60000,
                "cantidad": 2,
            },
            {
                "id_venta": 1,
                "fecha": "2026-01-10",
                "ciudad": "Armenia",
                "producto": "Mouse",
                "categoria": "Tecnologia",
                "precio_unitario": 60000,
                "cantidad": 2,
            },
        ])

        resultado = transformar(datos)

        # Debe conservar solamente una venta
        self.assertEqual(len(resultado), 1)

    def test_calcula_total_venta(self):
        datos = pd.DataFrame([{
            "id_venta": 2,
            "fecha": "2026-01-10",
            "ciudad": "Pereira",
            "producto": "Mouse",
            "categoria": "Tecnología",
            "precio_unitario": 60000,
            "cantidad": 3,
        }])

        resultado = transformar(datos)

        self.assertEqual(
            resultado.iloc[0]["total_venta"], 180000
        )

    def test_elimina_precios_negativos(self):
        # Una venta con precio negativo no debe pasar
        datos = pd.DataFrame([{
            "id_venta": 3,
            "fecha": "2026-01-10",
            "ciudad": "Cali",
            "producto": "Mouse",
            "categoria": "Tecnología",
            "precio_unitario": -100,
            "cantidad": 1,
        }])

        resultado = transformar(datos)

        self.assertEqual(len(resultado), 0)


if __name__ == "__main__":
    unittest.main()
