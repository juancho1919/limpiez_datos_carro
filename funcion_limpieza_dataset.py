

from gestion_archivos_lector import CorrectorCSVVentas

def corregir_ciudades(filas):
    for fila in filas:
        if "city" in fila:
            ciudad = fila["city"].strip().lower()
            if ciudad in ["bogotá", "bogota", "bogota d.c."]:
                fila["city"] = "Bogotá"
            elif ciudad in ["medellin", "medellín"]:
                fila["city"] = "Medellín"
            elif ciudad in ["cali", "santiago de cali"]:
                fila["city"] = "Cali"
    return filas
def corregir_deporte(filas):
    for fila in filas:
        if "product_category" in fila:
            deporte = fila["product_category"].strip().lower()
            if deporte in ["futbol", "fútbol"]:
                fila["product_category"] = "Fútbol"
            elif deporte == "baloncesto":
                fila["product_category"] = "Baloncesto"
            elif deporte in ["tenis", "tenis de campo"]:
                fila["product_category"] = "Tenis"
            elif deporte == "training":   # corregido
                fila["product_category"] = "Entrenamiento"
            elif deporte in ["running", "correr"]:  # corregido
                fila["product_category"] = "correr"
    return filas



def corregir_tamano(filas):
    for fila in filas:
        if "size" in fila:
            valor = fila["size"].strip()
            if valor == "" or valor.lower() in ["na", "null", "none"]:
                fila["size"] = "N/A"
    return filas

# Ejecución en cadena
corrector = CorrectorCSVVentas(
    "limpiez_datos_carro/dataset1_sports_store_sales.csv",
    "limpiez_datos_carro/correcion_dataset1_sports_store_sales.csv"
)

filas = corrector.leer_csv()
filas = corregir_ciudades(filas)  # Primera corrección
filas = corregir_tamano(filas)  
filas = corregir_deporte(filas)  # Segunda corrección
corrector.escribir_csv(filas)

