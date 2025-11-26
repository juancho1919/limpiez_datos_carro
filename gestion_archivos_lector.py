import csv
from datetime import datetime

class CorrectorCSVVentas:
    def __init__(self, archivo_entrada, archivo_salida, nuevos_encabezados=None):
        self.archivo_entrada = archivo_entrada
        self.archivo_salida = archivo_salida
        self.nuevos_encabezados = nuevos_encabezados  # Diccionario con cambios de nombres

    def leer_csv(self):
        """Lee el archivo CSV y devuelve las filas como lista de diccionarios."""
        with open(self.archivo_entrada, mode="r", newline="", encoding="utf-8") as f:
            lector = csv.DictReader(f)
            filas = list(lector)

            # Si hay mapeo de encabezados, renombramos las claves
            if self.nuevos_encabezados:
                filas_corregidas = []
                for fila in filas:
                    nueva_fila = {}
                    for clave, valor in fila.items():
                        nuevo_nombre = self.nuevos_encabezados.get(clave, clave)
                        nueva_fila[nuevo_nombre] = valor
                    filas_corregidas.append(nueva_fila)
                return filas_corregidas
            return filas

    def escribir_csv(self, filas):
        """Escribe una lista de diccionarios en un nuevo archivo CSV."""
        if not filas:
            print("No hay datos para escribir.")
            return

        with open(self.archivo_salida, mode="w", newline="", encoding="utf-8") as f:
            campos = filas[0].keys()  # Ahora ya son los nombres nuevos
            escritor = csv.DictWriter(f, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(filas)
        print(f"Archivo escrito correctamente en: {self.archivo_salida}")


# Ejemplo de uso
nuevos_nombres = {
    "sale_id": "ventas_id",
    "date": "fecha",
    "store": "almacen",
    "city": "ciudad",
    "product_category": "categoria_producto",
    "product_name": "nombre_producto",
    "size": "tamaño",
    "payment_method": "metodo_pago",
    "quantity": "cantidad",
    "unit_price": "precio_unitario",
    "discount_pct": "descuento_producto",
    "seller": "vendedor",
    "returned": "regreso"
}


corrector = CorrectorCSVVentas(
    "limpiez_datos_carro/dataset1_sports_store_sales.csv",
    "limpiez_datos_carro/correcion_dataset1_sports_store_sales.csv",
    nuevos_encabezados=nuevos_nombres
)

filas = corrector.leer_csv()
corrector.escribir_csv(filas)
