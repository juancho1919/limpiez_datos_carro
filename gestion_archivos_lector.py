import csv
from datetime import datetime

class CorrectorCSVVentas:
    def __init__(self, archivo_entrada, archivo_salida):
        self.archivo_entrada = archivo_entrada
        self.archivo_salida = archivo_salida

    def leer_csv(self):
        """Lee el archivo CSV y devuelve las filas como lista de diccionarios."""
        with open(self.archivo_entrada, mode="r", newline="", encoding="utf-8") as f:
            lector = csv.DictReader(f)
            return list(lector)

    def escribir_csv(self, filas):
        """Escribe una lista de diccionarios en un nuevo archivo CSV."""
        if not filas:
            print("No hay datos para escribir.")
            return

        with open(self.archivo_salida, mode="w", newline="", encoding="utf-8") as f:
            campos = filas[0].keys()  # Usa las claves del primer diccionario como encabezados
            escritor = csv.DictWriter(f, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(filas)
        print(f"Archivo escrito correctamente en: {self.archivo_salida}")

# Ejemplo de uso
corrector = CorrectorCSVVentas("limpiez_datos_carro/dataset1_sports_store_sales.csv", "limpiez_datos_carro/correcion_dataset1_sports_store_sales.csv")
filas = corrector.leer_csv()
corrector.escribir_csv(filas)
