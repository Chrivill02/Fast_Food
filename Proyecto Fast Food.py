#Espacio para Chris
import queue

class Producto:
    def __init__(self, nombre_ingrediente, costo, cantidad):
        self.nombre_ingrediente = nombre_ingrediente
        self.costo = costo
        self.cantidad = cantidad

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

class Inventario:
    def __init__(self):
        self.carne = Producto("Carne", 10, 40)
        self.queso = Producto("Queso", 5, 80)
        self.lechuga = Producto("Lechuga", 2, 70)
        self.tomate = Producto("Tomate", 3, 70)
        self.aderezo_clasico = Producto("Aderezo clasico", 4, 100)
        self.papas = Producto("Papas", 6, 80)
        self.bebida = Producto("Bebida", 6, 60)
        self.pan = Producto("Pan", 5, 150)
        self.cebolla_morada = Producto("Cebolla morada", 3, 90)
        self.cebolla_caramelizada = Producto("Cebolla caramelizada", 4, 80)
        self.aderezo_delacasa = Producto("Aderezo de la casa", 3, 150)
        self.pepinillos = Producto("Pepinillos", 5, 100)
        self.tocino = Producto("Tocino", 4, 80)

    def quitar_ingrediente(self, ingrediente):
        if ingrediente == "Carne":
            self.carne.cantidad -= 1
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
        elif ingrediente == "Pan":
            self.pan -= 1
        elif ingrediente == "Cebolla morada":
            self.cebolla_morada -=1
        elif ingrediente == "Cebolla caramelizada":
            self.cebolla_caramelizada -= 1
        elif ingrediente == "Aderezo de la casa":
            self.aderezo_delacasa -= 1
        elif ingrediente == "Pepinillos":
            self.pepinillos -= 1
        elif ingrediente == "Tocino":
            self.tocino -= 1

    def mostrar_inventario(self):
        print("Bienvenido al inventario! Lo que verás a continuacion es la cantidad de cada ingrediente")
        print("Carne: ", self.carne.cantidad)
        print("Queso: ", self.queso.cantidad)
        print("Lechuga: ", self.lechuga.cantidad)
        print("Tomate: ", self.tomate.cantidad)
        print("Aderezo clasico: ", self.aderezo_clasico.cantidad)
        print("Panes: ", self.pan.cantidad)
        print("Papas: ", self.papas.cantidad)
        print("Bebidas: ", self.bebida.cantidad)


cola = ColaPedidos()
inventario = Inventario()
pilaCarrito = []
opcion = 1
while opcion != 0:
    print("Bienvenido a Fast Food, Ingrese la opcion que desee")
    print("1. Gestión de pedidos")
    print("2. Seguimiento de Stock")
    print("3. Cola de pedidos")
    print("4. Facturación y pagos")
    print("5. Administracion de clientes")
    opcion = int(input(""))
    if opcion == 1:
        print("Bienvenido al menu")
        print("1. Combos")
        print("2. Personalizado")
        opcion_menu = int(input(""))
        if opcion_menu == 1:
            print("Bienvenido a los combos")
            print("1. Q30 Combo Hamburguesa clasica con papas y bebida")
            print("2. Q35 Combo Hamburguesa con tocino, papas y bebida")
            print("3. Q35 Combo Hamburguesa con doble queso, papas y bebida")
            print("4. Q40 Combo Hamburguesa de la casa, papas y bebida")
            opcion_combos = int(input(""))
            if opcion_combos == 1:
                inventario.quitar_ingrediente("Pan")
                inventario.quitar_ingrediente("Carne")
                inventario.quitar_ingrediente("Queso")
                inventario.quitar_ingrediente("Lechuga")
                inventario.quitar_ingrediente("Tomate")
                inventario.quitar_ingrediente("Aderezo clasico")
                inventario.quitar_ingrediente("Pepinillos")
                inventario.quitar_ingrediente("Papas")
                inventario.quitar_ingrediente("Bebida")
                cola.agregar_pedido("Combo Hamburguesa clasica")

        elif opcion_menu == 2:
            opcion_menuP = 1
            while opcion_menuP != 0:
                print("Bienvenido al apartado personalizado, selecciona que quieres agregar a tu orden")
                print("1. Hamburguesas")
                print("2. Papas")
                print("3. Bebidas")
                print("4. Ver orden")
                print("0. Finalizar orden")
                opcion_menuP = int(input(""))
                if opcion_menuP == 1:
                    opcion_ingredientes = 1
                    total = 5
                    listaHamburguesaP = []
                    listaHamburguesaP.append("Pan")
                    while opcion_ingredientes != 0:
                        print("Ingresa los ingredientes que deseas a tu orden (El pan se agrega automaticamente)")
                        print("1. Carne")
                        print("2. Queso")
                        print("3. Lechuga")
                        print("4. Tomate")
                        print("5. Cebolla morada")
                        print("6. Cebolla caramelizada")
                        print("7. Aderezo clasico")
                        print("8. Aderezo de la casa")
                        print("9. Tocino")
                        print("10. Pepinillos")
                        print("11. Ver lista de ingredientes para hamburguesa")
                        print("0. Finalizar")
                        opcion_ingredientes = int(input(""))
                        if opcion_ingredientes == 1:
                            listaHamburguesaP.append("Carne")
                            inventario.quitar_ingrediente("Carne")
                            total = total + inventario.carne.costo
                        elif opcion_ingredientes == 2:
                            listaHamburguesaP.append("Queso")
                            inventario.quitar_ingrediente("Queso")
                            total = total + inventario.queso.costo
                        elif opcion_ingredientes == 3:
                            listaHamburguesaP.append("Lechuga")
                            inventario.quitar_ingrediente("Lechuga")
                            total = total + inventario.lechuga.costo
                        elif opcion_ingredientes == 4:
                            listaHamburguesaP.append("Tomate")
                            inventario.quitar_ingrediente("Tomate")
                            total = total + inventario.tomate.costo
                        elif opcion_ingredientes == 5:
                            listaHamburguesaP.append("Cebolla morada")
                            inventario.quitar_ingrediente("Cebolla morada")
                            total = total + inventario.cebolla_morada.costo
                        elif opcion_ingredientes == 6:
                            listaHamburguesaP.append("Cebolla caramelizada")
                            inventario.quitar_ingrediente("Cebolla caramelizada")
                            total = total + inventario.cebolla_caramelizada.costo
                        elif opcion_ingredientes == 7:
                            listaHamburguesaP.append("Aderezo clasico")
                            inventario.quitar_ingrediente("Aderezo clasico")
                            total = total + inventario.aderezo_clasico.costo
                        elif opcion_ingredientes == 8:
                            listaHamburguesaP.append("Aderezo de la casa")
                            inventario.quitar_ingrediente("Aderezo de la casa")
                            total = total + inventario.aderezo_delacasa.costo
                        elif opcion_ingredientes == 9:
                            listaHamburguesaP.append("Tocino")
                            inventario.quitar_ingrediente("Tocino")
                            total = total + inventario.tocino.costo
                        elif opcion_ingredientes == 10:
                            listaHamburguesaP.append("Pepinillos")
                            inventario.quitar_ingrediente("Pepinillos")
                            total = total + inventario.pepinillos.costo
                        elif opcion_ingredientes == 11:
                            print("Ingredientes: ")
                            for i in range(0, len(listaHamburguesaP)):
                                print(listaHamburguesaP[i], end= " , ")
                            print("Total: ", total)



















#Espacio para Rodrigo