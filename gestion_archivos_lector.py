from funciones import Tienda

def menu():
    print("\n========== MENU ==========")
    print("1) Promedio de ventas por mes")
    print("2) Moda del vendedor por mes")
    print("3) Sucursal con más ventas")
    print("4) Registro cantidad de productos")
    print("5) Registro tallas")
    print("0) Salir")

# --- INICIO DEL PROGRAMA ---
tienda = Tienda(r"C:\Users\FORMACION\Downloads\26-11-25\dataset1_sports_store_sales.csv")

while True:
    menu()
    opcion = input("\nSeleccione opción: ")

    if opcion == "1":
        tienda.promedio_ventas_mes()
    elif opcion == "2":
        tienda.moda_vendedor_mes()
    elif opcion == "3":
        tienda.sucursal_mas_ventas()
    elif opcion == "4":
        tienda.registro_cantidad_productos()
    elif opcion == "5":
        tienda.registro_tallas()
    elif opcion == "0":
        print("\n👍 Saliendo…")
        break
    else:
        print("\n⚠️ Opción inválida")