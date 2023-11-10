def definir_pago():
    while True:
        tipo_pago = input("1. Tarjeta de credito\n"
                          "2. En efectivo\n"
                          "Seleccione su tipo de pago: ")

        if tipo_pago == "1":
            return "Tarjeta de credito"
        elif tipo_pago == "2":
            return "En efectivo"
        else:
            print("Escoja una opcion valida.")

def ordenamiento_burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - 1 - i):
            if lista[j].total > lista[j + 1].total:
                lista[j].total, lista[j + 1].total = lista[j + 1].total, lista[j].total


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
        print(f"  Numero del pedido: {self.no_pedido}")
        print(f"  Pedido: {self.producto.nombre}")
        print(f"  Total: Q{self.total}")
        print(f"  Tipo del pago: {self.tipo_pago}")
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

def IVA(total):
    IVA=(total*0.12)
    PrecioIVA=round(total+IVA,2)
    print("El IVA total es de: Q",IVA)
    print("Total con IVA incluido: Q",PrecioIVA)