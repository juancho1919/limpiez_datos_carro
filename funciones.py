

class AnalisisVentas:
    def __init__(self, archivo_csv):
        self.datos = []
        
    def promedio_ventas_por_mes(self):
        ventas_mes = {}
        for registro in self.datos:
            fecha = registro["date"]
            mes = fecha[5:7] + "-" + fecha[0:4]  # mm-aaaa
            total = float(registro["unit_price"]) * int(registro["quantity"])

            if mes not in ventas_mes:
                ventas_mes[mes] = {"total": 0, "conteo": 0}
            ventas_mes[mes]["total"] += total
            ventas_mes[mes]["conteo"] += 1

        print("Promedio de ventas por mes:")
        for mes in sorted(ventas_mes):
            info = ventas_mes[mes]
            promedio = info["total"] / info["conteo"]
            print(f"{mes}: ${promedio:,.2f}")

    def moda_vendedor_por_mes(self):
        vendedores_mes = {}
        for registro in self.datos:
            fecha = registro["date"]
            mes = fecha[5:7] + "-" + fecha[0:4]
            vendedor = registro["seller"].strip()
            if vendedor:
                if mes not in vendedores_mes:
                    vendedores_mes[mes] = {}
                if vendedor not in vendedores_mes[mes]:
                    vendedores_mes[mes][vendedor] = 0
                vendedores_mes[mes][vendedor] += 1

        print("Moda de vendedor por mes:")
        for mes in sorted(vendedores_mes):
            vendedores = vendedores_mes[mes]
            moda = None
            max_frecuencia = 0
            for nombre, frecuencia in vendedores.items():
                if frecuencia > max_frecuencia:
                    max_frecuencia = frecuencia
                    moda = nombre
            print(f"{mes}: {moda} ({max_frecuencia} ventas)")

    def sucursal_con_mas_ventas(self):
        sucursales = {}
        for registro in self.datos:
            sucursal = registro["store"].strip()
            total = float(registro["unit_price"]) * int(registro["quantity"])
            if sucursal not in sucursales:
                sucursales[sucursal] = 0
            sucursales[sucursal] += total

        mejor = None
        max_ventas = 0
        for sucursal, ventas in sucursales.items():
            if ventas > max_ventas:
                max_ventas = ventas
                mejor = sucursal

        print(f" Sucursal con más ventas: {mejor} (${max_ventas:,.2f})")

    def registro_productos(self):
        productos = {}
        for registro in self.datos:
            producto = registro["product_name"].strip()
            cantidad = int(registro["quantity"])
            if producto not in productos:
                productos[producto] = 0
            productos[producto] += cantidad

        print("Registro de productos:")
        for prod in sorted(productos):
            print(f"{prod}: {productos[prod]} unidades")

    def registro_tallas(self):
        tallas = {}
        for registro in self.datos:
            talla = registro["size"].strip()
            if talla:
                if talla not in tallas:
                    tallas[talla] = 0
                tallas[talla] += 1

        print("Registro de tallas:")
        for talla in sorted(tallas):
            print(f"{talla}: {tallas[talla]} registros")


