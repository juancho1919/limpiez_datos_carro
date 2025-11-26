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

    def promedio_ventas_mes(self):
        ventas = {}
        for fila in self.data:
            mes = fila.get("month")
            try:
                total = float(fila.get("price", 0)) * int(fila.get("quantity", 0))
            except:
                continue

            ventas.setdefault(mes, []).append(total)

        print("PROMEDIO DE VENTAS POR MES:")
        for mes, valores in ventas.items():
            print(f"• {mes}: {round(mean(valores),2)}")

    def moda_vendedor(self):
        vendedores = [fila.get("seller") for fila in self.data if fila.get("seller")]
        try:
            print("MODA DEL VENDEDOR (más repetido):", mode(vendedores))
        except:
            print("No hay moda (todos diferentes).")

    # Sucursal con más ventas totales
    def sucursal_mas_ventas(self):
        sucursales = {}
        for fila in self.data:
            suc = fila.get("store")
            try:
                total = float(fila.get("price", 0)) * int(fila.get("quantity", 0))
            except:
                continue
            sucursales[suc] = sucursales.get(suc, 0) + total

        max_sucursal = max(sucursales, key=sucursales.get)
        print("SUCURSAL CON MÁS VENTAS:")
        print(f"{max_sucursal} → {round(sucursales[max_sucursal],2)}")

    # Registro productos nombre-cantidad
    def registro_productos(self):
        print("REGISTRO DE PRODUCTOS (primeros 10):")
        for fila in self.data[:10]:
            print(f"{fila.get('product')} → {fila.get('quantity')} unidades")

    def registro_tallas(self):
        print("TALLAS ENCONTRADAS (primeros 10):")
        for fila in self.data[:10]:
            print(f"{fila.get('product')} → talla {fila.get('size')}")