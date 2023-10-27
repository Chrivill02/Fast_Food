#Espacio para Chris
import queue
class ColaPedidos:
    def __init__(self):
        self.cola = queue.Queue()
        self.listaPedidos = []
    def agregar_pedido(self, pedido):
        self.cola.put(pedido)
        self.listaPedidos.append(pedido)
        print("Se agregó correctamente el siguiente pedido: ", pedido)

    def preparar_pedido(self):
        print("Preparando: ", self.listaPedidos[0])
    def listo_para_servir(self):
        pedido = self.cola.get()
        print("Pedido: ", pedido, " listo para servir")
        self.listaPedidos.pop(0)

    def mostrar_inventario(self):
        print("Bienvenido al inventario! Lo que verás a continuacion es la cantidad de cada ingrediente")
        print("Carne: ", inventario.carne)
        print("Queso: ", inventario.queso)
        print("Lechuga: ", inventario.lechuga)
        print("Tomate: ", inventario.tomate)
        print("Aderezo clasico: ", inventario.aderezo_clasico)
        print("Papas: ", inventario.papas)
        print("Bebidas: ", inventario.bebida)
        
class Inventario:
    def __init__(self, carne, queso, lechuga, tomate, aderezo_clasico, papas, bebida):
        self.carne = carne
        self.queso = queso
        self.lechuga = lechuga
        self.tomate = tomate
        self.aderezo_clasico = aderezo_clasico
        self.papas = papas
        self.bebida = bebida


    def quitar_ingrediente(self, ingrediente):
        if ingrediente == "Carne":
            self.carne -= 1
        elif ingrediente == "Queso":
            self.queso -= 1
        elif ingrediente == "Lechuga":
            self.lechuga -= 1
        elif ingrediente == "Tomate":
            self.tomate -= 1
        elif ingrediente == "Aderezo clasico":
            self.aderezo_clasico -= 1
        elif ingrediente == "Papas":
            self.papas -= 1
        elif ingrediente == "Bebida":
            self.bebida -= 1


cola = ColaPedidos()
inventario = Inventario(20, 30, 40, 50, 30, 80, 70)
opcion = 1
while opcion != 0:
    print("Bienvenido a Fast Food, Ingrese la opcion que desee")
    print("1. Gestión de pedidos")
    print("2. Seguimiento de Stock")
    print("3. Menus y Precios")
    print("4. Cola de pedidos")
    print("5. Facturación y pagos")
    print("6. Administracion de clientes")
    opcion = int(input(""))
    if opcion == 1:
        print("Bienvenido al menu")
        print("1. Combos")
        print("2. Comida sin combo")
        print("3. Papas")
        print("4. Bebidas")
        opcion1 = int(input(""))
        if opcion1 == 1:
            print("Bienvenido a los combos")
            print("1. Combo Hamburguesas con papas y bebida")
            print("2. Combo Pollo frito con papas y bebida")
            print("3. Combo Pan con costilla, papas y bebida")
            opcion2 = int(input(""))
            if opcion2 == 1:
                print("Seleccione la hamburguesa")
                print("1. Hamburguesa clasica")
                print("2. Hamburguesa con Tocino")
                print("3. Hamburguesa con queso doble")
                print("4. Hamburguesa de la casa")
                opcion3 = int(input(""))
                if opcion3 == 1:
                    inventario.quitar_ingrediente("Carne")
                    inventario.quitar_ingrediente("Queso")
                    inventario.quitar_ingrediente("Lechuga")
                    inventario.quitar_ingrediente("Tomate")
                    inventario.quitar_ingrediente("Aderezo clasico")
                    inventario.quitar_ingrediente("Papas")
                    inventario.quitar_ingrediente("Bebida")
                    cola.agregar_pedido("Combo Hamburguesa clasica")














#Espacio para Rodrigo