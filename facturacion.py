def definir_pago():
    tipo_pago = input("1. Tarjeta de credito\n"
                      "2. En efectivo\n"
                      "Seleccione su tipo de pago: ")

    return tipo_pago


class Factura:
    def __init__(self, no_pedido, total, producto):
        self.no_pedido = no_pedido
        self.producto = producto
        self.total = total
        self.tipo_pago = definir_pago()
        self.cobro = False

    def mostrar_factura(self):
        print("\n")
        print("----------------------")
        print(f"    {self.no_pedido}")
        print(f"    {self.total}")
        print(f"    {self.tipo_pago}")
        print("----------------------")

    def cobrar(self):
        if not self.cobro:
            if self.tipo_pago == "Tarjeta de credito":
                numero_tarjeta = int(input("Ingrese el numero de su tarjeta: "))
                print("Se ha pagado su orden :D")
                numero_tarjeta = 0

            elif self.tipo_pago == "En efectivo":
                print("Pago realizado :D")
        else:
            print("El pago ya esta hecho :D")
