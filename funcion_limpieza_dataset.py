from gestion_archivos_lector import CorrectorCSVVentas

# Diccionario de cambios de nombres de columnas
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

def corregir_ciudades(filas):
    for fila in filas:
        if "ciudad" in fila:
            ciudad = fila["ciudad"].strip().lower()
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
            deporte = fila["categoria_producto"].strip().lower()
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
            valor = fila["tamaño"].strip()
            if valor == "" or valor.lower() in ["na", "null", "none"]:
                fila["tamaño"] = "N/A"
    return filas

# Ejecución en cadena
corrector = CorrectorCSVVentas(
    "limpiez_datos_carro/dataset1_sports_store_sales.csv",
    "limpiez_datos_carro/correcion_dataset1_sports_store_sales.csv",
    nuevos_encabezados=nuevos_nombres
)

filas = corrector.leer_csv()
filas = corregir_ciudades(filas)     # Corrección de ciudades
filas = corregir_tamano(filas)       # Corrección de tamaños
filas = corregir_deporte(filas)      # Corrección de deportes
corrector.escribir_csv(filas)

