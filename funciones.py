import csv
from statistics import mean, mode

class Tienda:

    def __init__(self, ruta_csv):
        self.ruta = ruta_csv
        self.data = []
        self.cargar_csv()

    def cargar_csv(self):
        try:
            with open(self.ruta, "r", encoding="utf-8-sig") as f:
                lector = csv.DictReader(f)
                self.data = list(lector)
            print(f"CSV cargado correctamente → {len(self.data)} registros.")
        except Exception as e:
            print("Error al leer CSV:", e)

    # 1 Promedio de ventas por mes (precio * cantidad)
    def promedio_ventas_mes(self):
        ventas = {}
        for fila in self.data:
            fecha = fila.get("fecha", "")
            if not fecha:
                continue

            mes = fecha[:7]  # YYYY-MM

            try:
                precio = float(fila.get("precio_unitario", 0))
                cantidad = int(fila.get("cantidad", 0))
                total = precio * cantidad
            except:
                continue

            ventas.setdefault(mes, []).append(total)

        print("PROMEDIO DE VENTAS POR MES:")
        for mes, valores in ventas.items():
            print(f"• {mes}: ${round(mean(valores), 2)}")

    # 2 Moda vendedor
    def moda_vendedor(self):
        vendedores = [fila.get("vendedor") for fila in self.data if fila.get("vendedor")]
        try:
            print("VENDEDOR MÁS REPETIDO:", mode(vendedores))
        except:
            print("No hay moda (todos diferentes).")

    # 3 Sucursal con más ventas
    def sucursal_mas_ventas(self):
        sucursales = {}
        for fila in self.data:
            suc = fila.get("almacen")
            try:
                total = float(fila.get("precio_unitario", 0)) * int(fila.get("cantidad", 0))
            except:
                continue
            sucursales[suc] = sucursales.get(suc, 0) + total

        max_sucursal = max(sucursales, key=sucursales.get)
        print("SUCURSAL CON MÁS VENTAS:")
        print(f"{max_sucursal} → ${round(sucursales[max_sucursal],2)}")

    # 4 Total de unidades por producto
    def registro_productos(self):
        productos = {}

        for fila in self.data:
            nombre = fila.get("nombre_producto")

            # Ignorar filas sin nombre
            if not nombre:
                continue

            try:
                cantidad = int(fila.get("cantidad", 0))
            except:
                continue

            productos[nombre] = productos.get(nombre, 0) + cantidad

        print("TOTAL DE PRODUCTOS VENDIDOS:")
        for producto, total in productos.items():
            print(f"- {producto}: {total} unidades")

    # 5 Registro tallas
    def registro_tallas(self):
        print("TALLAS ENCONTRADAS (primeros 10):")
        for fila in self.data[:10]:
            print(f"{fila.get('nombre_producto')} → talla {fila.get('tamaño')}")