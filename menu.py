from funciones import Tienda

# Usamos la misma dirección del archivo corregido
RUTA_CSV = r"C:\Users\User\Documents\correcion\limpiez_datos_carro\correcion_dataset1_sports_store_sales.csv"

# Instanciamos la clase Tienda con el CSV corregido
tienda = Tienda(RUTA_CSV)

def menu():
    print("\n=========== MENU ===========")
    print("1. Promedio de ventas por mes")
    print("2. Moda del vendedor")
    print("3. Sucursal con más ventas")
    print("4. Registro nombre - cantidad")
    print("5. Registro tallas")
    print("0. Salir")
    return input("Seleccione opción: ")

while True:
    opcion = menu()

    if opcion == "1":
        print("\n--- Promedio de ventas por mes ---")
        tienda.promedio_ventas_mes()

    elif opcion == "2":
        print("\n--- Moda del vendedor ---")
        tienda.moda_vendedor()

    elif opcion == "3":
        print("\n--- Sucursal con más ventas ---")
        tienda.sucursal_mas_ventas()

    elif opcion == "4":
        print("\n--- Registro nombre - cantidad ---")
        tienda.registro_productos()

    elif opcion == "5":
        print("\n--- Registro tallas ---")
        tienda.registro_tallas()

    elif opcion == "0":
        print("Programa finalizado")
        break

    else:
        print("Opción inválida.")

    input("\nPresione Enter para continuar...")
