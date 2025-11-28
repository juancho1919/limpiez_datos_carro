import csv
from datetime import datetime 

class Funcion_Limpieza_Dataset:
    def __init__(self, archivo_entrada, archivo_salida):
        self.archivo_entrada = archivo_entrada
        self.archivo_salida = archivo_salida

    def leer_csv(self):
        nuevos_encabezados = {
            "sale_id": "Ventas_id",
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

        with open(self.archivo_entrada, mode="r", newline="", encoding="utf-8") as f:
            lector = csv.DictReader(f)
            filas = list(lector)

            # Aplicar el mapeo de encabezados
            filas_corregidas = []
            for fila in filas:
                nueva_fila = {}
                for clave, valor in fila.items():
                    nuevo_nombre = nuevos_encabezados.get(clave, clave)
                    nueva_fila[nuevo_nombre] = valor
                filas_corregidas.append(nueva_fila)
            return filas_corregidas

    def escribir_csv(self, filas):
        """Escribe una lista de diccionarios en un nuevo archivo CSV."""
        if not filas:
            print("No hay datos para escribir.")
            return

        with open(self.archivo_salida, mode="w", newline="", encoding="utf-8") as f:
            campos = filas[0].keys()  # Ya son los nombres nuevos
            escritor = csv.DictWriter(f, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(filas)
        print(f"Archivo escrito correctamente en: {self.archivo_salida}")


# Funciones de corrección
def eliminar_espacios(filas):
    for fila in filas:
        for clave, valor in fila.items():
            if isinstance(valor, str):
                fila[clave] = valor.strip()
    return filas

def corregir_ciudades(filas):
    for fila in filas:
        if "ciudad" in fila:
            ciudad = fila["ciudad"].lower()
            if ciudad in ["bogotá", "bogota", "bogota d.c."]:
                fila["ciudad"] = "Bogotá"
            elif ciudad in ["medellin", "medellín"]:
                fila["ciudad"] = "Medellín"
            elif ciudad in ["cali", "santiago de cali"]:
                fila["ciudad"] = "Cali"
    return filas

def corregir_deporte(filas):
    for fila in filas:
        if "categoria_producto" in fila:
            deporte = fila["categoria_producto"].lower()
            if deporte in ["futbol", "fútbol"]:
                fila["categoria_producto"] = "Fútbol"
            elif deporte == "baloncesto":
                fila["categoria_producto"] = "Baloncesto"
            elif deporte in ["tenis", "tenis de campo"]:
                fila["categoria_producto"] = "Tenis"
            elif deporte == "training":
                fila["categoria_producto"] = "Entrenamiento"
            elif deporte in ["running", "correr"]:
                fila["categoria_producto"] = "Correr"
    return filas

def corregir_tamano(filas):
    for fila in filas:
        if "tamaño" in fila:
            valor = fila["tamaño"]
            if valor == "" or valor.lower() in ["na", "null", "none"]:
                fila["tamaño"] = "N/A"
    return filas

def corregir_vendedor(filas):
    for fila in filas:
        if "vendedor" in fila:
            valor = fila["vendedor"]
            if valor == "" or valor.lower() in ["na", "null", "none"]:
                fila["vendedor"] = "NULL"
    return filas

def corregir_nombre_producto(filas):
    """Quita los espacios iniciales de la columna nombre_producto."""
    for fila in filas:
        if "nombre_producto" in fila and isinstance(fila["nombre_producto"], str):
            fila["nombre_producto"] = fila["nombre_producto"].lstrip()
    return filas


# Ejecución en cadena
corrector = Funcion_Limpieza_Dataset(
    "limpiez_datos_carro/dataset1_sports_store_sales.csv",
    "limpiez_datos_carro/correcion_dataset1_sports_store_sales.csv"
)

filas = corrector.leer_csv()

if filas:   # Solo si hay datos
    filas = eliminar_espacios(filas)        # Limpieza general de espacios
    filas = corregir_ciudades(filas)        # Corrección de ciudades
    filas = corregir_tamano(filas)          # Corrección de tamaños
    filas = corregir_deporte(filas)         # Corrección de deportes
    filas = corregir_vendedor(filas)        # Corrección de vendedores
    filas = corregir_nombre_producto(filas) # Corrección de nombre_producto
    corrector.escribir_csv(filas)
else:
    print("El archivo de entrada está vacío o no se pudo leer correctamente.")
