from funciones import AnalisisVentas


archivo_csv = "correcion_dataset1_sports_store_sales.csv"

analisis = AnalisisVentas(archivo_csv)

def mostrar_menu():
    while True:
        print("\n--- MENÚ DE ANÁLISIS DE VENTAS ---")
        print("1. Promedio de ventas por mes")
        print("2. Moda de vendedor por mes")
        print("3. Sucursal con más ventas")
        print("4. Registro de cantidad de productos")
        print("5. Registro de tallas")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            analisis.promedio_ventas_por_mes()
        elif opcion == "2":
            analisis.moda_vendedor_por_mes()
        elif opcion == "3":
            analisis.sucursal_con_mas_ventas()
        elif opcion == "4":
            analisis.registro_productos()
        elif opcion == "5":
            analisis.registro_tallas()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    mostrar_menu()
