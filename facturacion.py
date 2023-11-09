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
def DatosCliente():
    Encabezados="Nombre;NIT;Numero de Telefono; Direccion, Compras, Frecuente"
    Clientes={}
    cliente=input("Ingrese el NIT del cliente: ")
    if cliente not in Clientes:
        print("Nuevo cliente")
        nombre=input("Ingrese el nombre del nuevo cliente: ")
        direccion=input("Ingrese la dirección del nuevo cliente: ")
        telefono=input("Ingrese el número de teléfono del nuevo cliente: ")
        Compras=0
        Frecuente= False
        Clientes[cliente]={"Nombre":nombre,"Direccion":direccion,"Telefono":telefono,"Compras":Compras, "Frecuente":Frecuente}
    else:
        informacion = Clientes[cliente]
        print("Cliente:", informacion["Nombre"])
        print("Numero de contacto:", informacion["Telefono"])
        print("Direccion:", informacion["Direccion"])
        opcion=input("La informacion es correcta? presione 1 para confirmar y 2 para modificar: ")
        if opcion == "1":
            print("Iniciar proceso de facturacion")
            Compras_Realizadas = informacion["Compras"]
            Compras_Realizadas += 1
            Clientes[cliente]["Compras"] = Compras_Realizadas
            if Compras_Realizadas >= 50:
                Frecuente= True
                print("Cliente frecuente, aplicar descuento del 5%")



    cliente=input("Ingrese el NIT del cliente: ")
    if cliente not in Clientes:
        print("Nuevo cliente")
        nombre=input("Ingrese el nombre del nuevo cliente: ")
        direccion=input("Ingrese la dirección del nuevo cliente: ")
        telefono=input("Ingrese el número de teléfono del nuevo cliente: ")
        Compras=0
        Frecuente= False
        Clientes[cliente]={"Nombre":nombre,"Direccion":direccion,"Telefono":telefono,"Compras":Compras, "Frecuente":Frecuente}
    else:
        informacion = Clientes[cliente]
        print("Cliente:", informacion["Nombre"])
        print("Numero de contacto:", informacion["Telefono"])
        print("Direccion:", informacion["Direccion"])
        opcion=input("La informacion es correcta? presione 1 para confirmar y 2 para modificar: ")
        if opcion == "1":
            print("Iniciar proceso de facturacion")
            Compras_Realizadas = informacion["Compras"]
            Compras_Realizadas += 1
            Clientes[cliente]["Compras"] = Compras_Realizadas
            if Compras_Realizadas >= 50:
                Frecuente= True
                print("Cliente frecuente, aplicar descuento del 5%")


        elif opcion == "2":
            print("1. Nombre del cliente")
            print("2. Numero de contacto")
            print("3. Direccion de entrega")
            opcion2=input("Seleccione el dato que desea modificar: ")
            if opcion2=="1":
                Nuevo=input("Ingrese el Nombre: ")
                Clientes[cliente]["Nombre"]=Nuevo
            elif opcion2=="2":
                Nuevo=input("Ingrese el numero de telefono: ")
                Clientes[cliente]["Telefono"]=Nuevo
            elif opcion2=="3":
                Nuevo=input("Ingrese la nueva direccion: ")
                Clientes[cliente]["Direccion"]=Nuevo
            else:
                print("Por favor seleccione una opcion valida")
        else:

            print("Por favor ingrese una opcion valida")

def IVA(total):
    IVA=(total*0.12)
    PrecioIVA=round(total+IVA,2)
    print("El IVA total es de: Q",IVA)
    print("Total con IVA incluido: Q",PrecioIVA)
def pedidos():
    Precios=[]
    Pedidos=[]
    Total=0
    opcion=input("Desea agregar un nuevo pedido? S/N \n")
    while opcion=="S" or opcion == "s":
        if opcion=="S" or opcion == "s":
            pedido=input("Ingrese su pedido: ")
            Pedidos.append(pedido)
            precio=float(input("Ingrese el precio del pedido: "))
            Precios.append(precio)
            opcion = input("Desea agregar un nuevo pedido? S/N \n")
    for i in Pedidos:
        print (i)
    for i in Precios:
        Total=Total+i

    print(Total)
    print(IVA(Total))