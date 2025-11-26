from funciones import Tienda

RUTA_CSV = r"C:\Users\FORMACION\Downloads\26-11-25\limpiez_datos_carro\correcion_dataset1_sports_store_sales.csv"

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
        tienda.promedio_ventas_mes()

    elif opcion == "2":
        tienda.moda_vendedor()

    elif opcion == "3":
        tienda.sucursal_mas_ventas()

    elif opcion == "4":
        tienda.registro_productos()

    elif opcion == "5":
        tienda.registro_tallas()

    elif opcion == "0":
        print("Programa finalizado")
        break

    else:
        print("Opción inválida.")