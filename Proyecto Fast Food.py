#Espacio para Chris
import queue
#Este numero es para saber el numero de orden (de los menus personalizados), es como un contador
num_ordenP = 0
num_orden = 0

#Clase donde instancio todos los ingredientes, bebidas, papas etc

class Producto:
    def __init__(self, nombre_ingrediente, costo, cantidad):
        self.nombre_ingrediente = nombre_ingrediente
        self.costo = costo
        #La cantidad se refiere a cuanto de cada cosa habrá al inici0
        self.cantidad = cantidad

#Clase cola para ir agregando las acciones
class ColaPedidos:

    def __init__(self):
        self.cola = queue.Queue()
        #Lista para mostrar datos, ya que con cola si hago un get para mostrar lo retira de la cola
        self.listaPedidos = []

    #Aqui como parametro un objeto de la clase pedido
    def agregar_pedido(self, pedido):
        self.cola.put(pedido)
        self.listaPedidos.append(pedido)
        print("Se agregó correctamente el siguiente pedido: ", pedido.nombre)


    def preparar_pedido(self):
        try:
            if self.listaPedidos[0].estado == "Pendiente":
                print("Preparando: ", self.listaPedidos[0].nombre)
                self.listaPedidos[0].estado = "En preparación"
            elif self.listaPedidos[0].estado == "En preparación":
                print("El pedido ya se encuentra en preparación")
        except IndexError:
            print("No hay pedidos para preparar")
    def busqueda_secuencial(self, orden):
        for i, pedido in enumerate(self.listaPedidos):
            if pedido.num_orden == orden:
                return i
        return -1
#Verificaciones para ver si se puede preparar o servir el pedido
    def listo_para_servir(self):
        try:
            if self.listaPedidos[0].estado == "Pendiente":
                print("El pedido aún no se ha preparado")
            elif self.listaPedidos[0].estado == "En preparación":
                pedido = self.cola.get()
                print("Pedido: ", pedido.nombre, " listo para servir")
                self.listaPedidos.pop(0)
                return pedido
        except IndexError:
            print("No hay pedidos para servir")

#Aqui es donde uso la lista de pedidos
    def mostrar_elementos_cola(self):
        if len(self.listaPedidos) == 0:
            print("Cola vacia")
        for i in range(0, len(self.listaPedidos)):
            print(self.listaPedidos[i].nombre, ". Estado: ", self.listaPedidos[i].estado)

#Clase inventario en donde estará todo el stock
class Inventario:
    def __init__(self):
        self.lista = []
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
#El contador me servirá para saber si el menú se puede realizar o hat una cantidad (contador) de ingredientes faltantes
    #def agregar_ingrediente():
    #self.lista.append(Producto("Nombre", costo, cantidad))
    def quitar_ingrediente(self, ingrediente, contador):
        if ingrediente == "Carne":
            if self.carne.cantidad == 0:
                print("No hay carne disponible")
                return  1
            else:
                self.carne.cantidad -= 1
                return 0
        elif ingrediente == "Queso":
            if self.queso.cantidad == 0:
                print("No hay queso disponible")
                return 1
            else:
                self.queso.cantidad -= 1
                return 0
        elif ingrediente == "Lechuga":
            if self.lechuga.cantidad == 0:
                print("No hay lechuga disponible")
                return 1
            else:
                self.lechuga.cantidad -= 1
                return 0
        elif ingrediente == "Tomate":
            if self.tomate.cantidad == 0:
                print("No hay tomate disponible")
                return 1
            else:
                self.tomate.cantidad -= 1
                return 0
        elif ingrediente == "Aderezo clasico":
            if self.aderezo_clasico.cantidad == 0:
                print("No hay aderezo clasico disponible")
                return 1
            else:
                self.aderezo_clasico.cantidad -= 1
                return 0
        elif ingrediente == "Papas":
            if self.papas.cantidad == 0:
                print("No hay papas disponible")
                return 1
            else:
                self.papas.cantidad -= 1
                return 0
        elif ingrediente == "Bebida":
            if self.bebida.cantidad == 0:
                print("No hay bebidas disponible")
                return 1
            else:
                self.bebida.cantidad -= 1
                return 0
        elif ingrediente == "Pan":
            if self.pan.cantidad == 0:
                print("No hay pan disponible")
                return 1
            else:
                self.pan.cantidad -= 1
                return 0
        elif ingrediente == "Cebolla morada":
            if self.cebolla_morada.cantidad == 0:
                print("No hay cebolla morada disponible")
                return 1
            else:
                self.cebolla_morada.cantidad -=1
                return 0
        elif ingrediente == "Cebolla caramelizada":
            if self.cebolla_caramelizada.cantidad == 0:
                print("No hay cebolla caramelizada disponible")
                return 1
            else:
                self.cebolla_caramelizada.cantidad -= 1
                return 0
        elif ingrediente == "Aderezo de la casa":
            if self.aderezo_delacasa.cantidad == 0:
                print("No hay aderezo de la casa disponible")
                return 1
            else:
                self.aderezo_delacasa.cantidad -= 1
                return 0
        elif ingrediente == "Pepinillos":
            if self.pepinillos.cantidad == 0:
                print("No hay pepinillos disponible")
                return 1
            else:
                self.pepinillos.cantidad -= 1
                return 0
        elif ingrediente == "Tocino":
            if self.tocino.cantidad == 0:
                print("No hay tocino disponible")
                return 1
            else:
                self.tocino.cantidad -= 1
                return 0

    def mostrar_inventario(self):
        print("Bienvenido al inventario! Lo que verás a continuacion es la cantidad de cada ingrediente")
        print("Carne: ", self.carne.cantidad)
        print("Queso: ", self.queso.cantidad)
        print("Lechuga: ", self.lechuga.cantidad)
        print("Tomate: ", self.tomate.cantidad)
        print("Aderezo clasico: ", self.aderezo_clasico.cantidad)
        print("Panes: ", self.pan.cantidad)
        print("Cebollada Morada: ", self.cebolla_morada.cantidad)
        print("Cebolla Caramelizada: ", self.cebolla_caramelizada.cantidad)
        print("Aderezo de la casa: ", self.aderezo_delacasa.cantidad)
        print("Pepinillos: ", self.pepinillos.cantidad)
        print("Tocinos: ", self.tocino.cantidad)
        print("Papas: ", self.papas.cantidad)
        print("Bebidas: ", self.bebida.cantidad)


#Clase pedido, ya que tiene nombre y estado
class Pedido:
    def __init__(self, nombre, estado, num_orden, total):
        self.nombre = nombre
        self.estado = estado
        self.num_orden = num_orden
        self.total = total
def quitar_ingredientesC1():
    contador = 0
    contador = contador + inventario.quitar_ingrediente("Pan", contador)
    contador = contador + inventario.quitar_ingrediente("Carne", contador)
    contador = contador + inventario.quitar_ingrediente("Queso", contador)
    contador = contador + inventario.quitar_ingrediente("Lechuga", contador)
    contador = contador + inventario.quitar_ingrediente("Tomate", contador)
    contador = contador + inventario.quitar_ingrediente("Aderezo clasico", contador)
    contador = contador + inventario.quitar_ingrediente("Pepinillos", contador)
    contador = contador + inventario.quitar_ingrediente("Papas", contador)
    contador = contador + inventario.quitar_ingrediente("Bebida", contador)
    return contador

def quitar_ingredientesC2():
    contador = 0
    contador = inventario.quitar_ingrediente("Pan", contador) + contador
    contador = inventario.quitar_ingrediente("Carne", contador) + contador
    contador = inventario.quitar_ingrediente("Queso", contador) + contador
    contador = inventario.quitar_ingrediente("Lechuga", contador) + contador
    contador = inventario.quitar_ingrediente("Tomate", contador) + contador
    contador = inventario.quitar_ingrediente("Aderezo clasico", contador) + contador
    contador = inventario.quitar_ingrediente("Tocino", contador) + contador
    contador = inventario.quitar_ingrediente("Papas", contador) + contador
    contador = inventario.quitar_ingrediente("Bebida", contador) + contador
    return contador

def quitar_ingredientesC3():
    contador = 0
    contador = inventario.quitar_ingrediente("Pan", contador) + contador
    contador = inventario.quitar_ingrediente("Carne", contador) + contador
    contador = inventario.quitar_ingrediente("Queso", contador) + contador
    contador = inventario.quitar_ingrediente("Queso", contador) + contador
    contador = inventario.quitar_ingrediente("Lechuga", contador) + contador
    contador = inventario.quitar_ingrediente("Tomate", contador) + contador
    contador = inventario.quitar_ingrediente("Aderezo clasico", contador) + contador
    contador = inventario.quitar_ingrediente("Cebolla morada", contador) + contador
    contador = inventario.quitar_ingrediente("Papas", contador) + contador
    contador = inventario.quitar_ingrediente("Bebida", contador) + contador
    return contador

def quitar_ingredientesC4():
    contador = 0
    contador = inventario.quitar_ingrediente("Pan", contador) + contador
    contador = inventario.quitar_ingrediente("Carne", contador) + contador
    contador = inventario.quitar_ingrediente("Queso", contador) + contador
    contador = inventario.quitar_ingrediente("Cebolla caramelizada", contador) + contador
    contador = inventario.quitar_ingrediente("Lechuga", contador) + contador
    contador = inventario.quitar_ingrediente("Tomate", contador) + contador
    contador = inventario.quitar_ingrediente("Aderezo de la casa", contador) + contador
    contador = inventario.quitar_ingrediente("Pepinillos", contador) + contador
    contador = inventario.quitar_ingrediente("Papas", contador) + contador
    contador = inventario.quitar_ingrediente("Bebida", contador) + contador
    return contador

#---------------------------------------------------------Menú-----------------------------------------------------------

cola = ColaPedidos()
inventario = Inventario()
opcion = 1
while opcion != 0:
    print("Bienvenido a Fast Food, Ingrese la opcion que desee")
    print("1. Gestión de pedidos")
    print("2. Seguimiento de Stock")
    print("3. Cola de pedidos")
    print("4. Facturación y pagos")
    print("5. Administracion de clientes")
    print("0. Salir")
    try:
        opcion = int(input(""))
    except ValueError:
        print("Error, ingrese solo numeros")
        opcion = 7
    if opcion == 1:
        print("Bienvenido al menu")
        print("1. Combos")
        print("2. Personalizado")
        try:
            opcion_menu = int(input(""))
        except ValueError:
            print("Error, ingrese solo numeros")
            opcion_menu = 3
        if opcion_menu == 1:

            print("Bienvenido a los combos")
            print("1. Q30 Combo Hamburguesa clasica con papas y bebida")
            print("2. Q35 Combo Hamburguesa con tocino, papas y bebida")
            print("3. Q35 Combo Hamburguesa con doble queso, papas y bebida")
            print("4. Q40 Combo Hamburguesa de la casa, papas y bebida")
            try:
                opcion_combos = int(input(""))
            except ValueError:
                print("Error, ingrese solo numeros")
                opcion_combos = 5
            if opcion_combos == 1:
                contador = quitar_ingredientesC1()
                if contador == 0:
                    num_orden += 1
                    total = 30
                    print("Orden: ", num_orden, " Agregada!")
                    pedido = Pedido("Combo Hamburguesa clasica", "Pendiente", num_orden, total)
                    cola.agregar_pedido(pedido)


                else:
                    print("No hay ingredientes suficientes!")
                    print("Faltaron: ", contador, " ingredientes")
            elif opcion_combos == 2:
                contador = quitar_ingredientesC2()
                if contador == 0:
                    num_orden += 1
                    total = 35
                    print("Orden: ", num_orden, " Agregada!")
                    pedido = Pedido("Combo Hamburguesa con tocino", "Pendiente", num_orden, total)
                    cola.agregar_pedido(pedido)
                else:
                    print("No hay ingredientes suficientes!")
                    print("Faltaron: ", contador, " ingredientes")
            elif opcion_combos == 3:
                contador = quitar_ingredientesC3()
                if contador == 0:
                    num_orden += 1
                    total = 35
                    print("Orden: ", num_orden, " Agregada!")
                    pedido = Pedido("Combo Hamburguesa con doble queso", "Pendiente", num_orden, total)
                    cola.agregar_pedido(pedido)
                else:
                    print("No hay ingredientes suficientes!")
                    print("Faltaron: ", contador, " ingredientes")
            elif opcion_combos == 4:
                contador = quitar_ingredientesC4()
                if contador == 0:
                    num_orden += 1
                    total = 40
                    print("Orden: ", num_orden, " Agregada!")
                    pedido = Pedido("Combo Hamburguesa de la casa", "Pendiente", num_orden, total)
                    cola.agregar_pedido(pedido)
                else:
                    print("No hay ingredientes suficientes!")
                    print("Faltaron: ", contador, " ingredientes")
        elif opcion_menu == 2:
            opcion_menuP = 1
            #El apartado personalizado consta de una hamburguesa con los ingredientes que el cliente desee
            #Hasta que se finalize la orden el cliente podrá agregar cuantos ingredientes quiera
            total_dinero = 0
            listaOrdenP = []
            while opcion_menuP != 0:
                print("Bienvenido al apartado personalizado, selecciona que quieres agregar a tu orden")
                print("1. Hamburguesas")
                print("2. Papas")
                print("3. Bebidas")
                print("4. Ver orden")
                print("0. Finalizar orden")
                #Lista de los ingredientes de la hamburguesa
                try:
                    opcion_menuP = int(input(""))
                except ValueError:
                    print("Error, ingrese solo numeros")
                    opcion_menuP = 6
                if opcion_menuP == 1:
                    opcion_ingredientes = 1
                    listaHamburguesaP = []
                    #Tengo una listaOrden para que cuando se muestren las ordenes aparezca hamburugesa personaliza,
                    #Bebida, papas o solo bebida o solo papas
                    contadorP2 = inventario.quitar_ingrediente("Pan", 0)
                    if contadorP2 == 0:
                        listaOrdenP.append("Hamburguesa Personalizada")
                        listaHamburguesaP.append("Pan")
                        total_dinero = total_dinero + inventario.pan.costo
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
                            try:
                                opcion_ingredientes = int(input(""))
                            except ValueError:
                                print("Error, ingrese solo numeros")
                                opcion_menu = 15
                            if opcion_ingredientes == 1:
                                contadorP2 = inventario.quitar_ingrediente("Carne", 0)
                                if contadorP2 == 0:
                                    listaHamburguesaP.append("Carne")
                                    total_dinero = total_dinero + inventario.carne.costo
                                    print("Se agregó la carne correctamente")
                            elif opcion_ingredientes == 2:
                                contadorP2 = inventario.quitar_ingrediente("Queso", 0)
                                if contadorP2 == 0:
                                    listaHamburguesaP.append("Queso")
                                    total_dinero = total_dinero + inventario.queso.costo
                                    print("Se agregó el queso correctamente")
                            elif opcion_ingredientes == 3:
                                contadorP2 = inventario.quitar_ingrediente("Lechuga", 0)
                                if contadorP2 == 0:
                                    listaHamburguesaP.append("Lechuga")
                                    total_dinero = total_dinero + inventario.lechuga.costo
                                    print("Se agregó lechuga correctamente")
                            elif opcion_ingredientes == 4:
                                contadorP2 = inventario.quitar_ingrediente("Tomate", 0)
                                if contadorP2 == 0:
                                    listaHamburguesaP.append("Tomate")
                                    total_dinero = total_dinero + inventario.tomate.costo
                                    print("Se agregó el tomate correctamente")
                            elif opcion_ingredientes == 5:
                                contadorP2 = inventario.quitar_ingrediente("Cebolla morada", 0)
                                if contadorP2 == 0:
                                    listaHamburguesaP.append("Cebolla morada")
                                    total_dinero = total_dinero + inventario.cebolla_morada.costo
                                    print("Se agregó cebolla morada correctamente")
                            elif opcion_ingredientes == 6:
                                contadorP2 = inventario.quitar_ingrediente("Cebolla caramelizada", 0)
                                if contadorP2 == 0:
                                    listaHamburguesaP.append("Cebolla caramelizada")
                                    total_dinero = total_dinero + inventario.cebolla_caramelizada.costo
                                    print("Se agregó cebolla caramelizada correctamente")
                            elif opcion_ingredientes == 7:
                                contadorP2 = inventario.quitar_ingrediente("Aderezo clasico", 0)
                                if contadorP2 == 0:
                                    listaHamburguesaP.append("Aderezo clasico")
                                    total_dinero = total_dinero + inventario.aderezo_clasico.costo
                                    print("Se agregó aderezo clasico correctamente")
                            elif opcion_ingredientes == 8:
                                contadorP2 = inventario.quitar_ingrediente("Aderezo de la casa" , 0)
                                if contadorP2 == 0:
                                    listaHamburguesaP.append("Aderezo de la casa")
                                    total_dinero = total_dinero + inventario.aderezo_delacasa.costo
                                    print("Se agregó aderezo de la casa correctamente")
                            elif opcion_ingredientes == 9:
                                contadorP2 = inventario.quitar_ingrediente("Tocino", 0)
                                if contadorP2 == 0:
                                    listaHamburguesaP.append("Tocino")
                                    total_dinero = total_dinero + inventario.tocino.costo
                                    print("Se agregó tocino correctamente")
                            elif opcion_ingredientes == 10:
                                contadorP2 = inventario.quitar_ingrediente("Pepinillos", 0)
                                if contadorP2 == 0:
                                    listaHamburguesaP.append("Pepinillos")
                                    total_dinero = total_dinero + inventario.pepinillos.costo
                                    print("Se agregaron pepinillos correctamente")
                            elif opcion_ingredientes == 11:
                                print("Ingredientes: ")
                                for i in range(0, len(listaHamburguesaP)):
                                    print(listaHamburguesaP[i], end=" , ")
                                print("Total: ", total_dinero)
                    else:
                        print("No hay pan para hamburguesa")
                elif opcion_menuP == 2:
                    #Aqui si se agregan las papas tiene que ver con la orden, no con la otra lista de ingredientes
                    contadorP2 = inventario.quitar_ingrediente("Papas", 0)
                    if contadorP2 == 0:
                        listaOrdenP.append("Porcion de papas")
                        total_dinero = total_dinero + inventario.pepinillos.costo
                        print("Se agregaron papas correctamente")
                elif opcion_menuP == 3:
                    #Lo mismo de la orden pasa con la bebida
                    contadorP2 = inventario.quitar_ingrediente("Bebida", 0)
                    listaOrdenP.append("Bebida")
                    total_dinero = total_dinero + inventario.bebida.costo
                    print("Se agregó bebida correctamente")
                elif opcion_menuP == 4:
                    try:
                        for i in range(0, len(listaOrdenP)):
                            print(listaOrdenP[i], end=" , ")
                        print("Total: ", total_dinero)
                    except IndexError:
                        print("No hay ningun elemento agregado a la orden")
                elif opcion_menuP == 0:
                    #Aqui se usa la lista de la orden con el numero de orden
                    num_orden += 1
                    print("Orden: ", num_orden, " Agregada!")
                    pedido = Pedido("Menú personalizado: " + str(num_ordenP), "Pendiente", num_orden, total_dinero)
                    cola.agregar_pedido(pedido)



    elif opcion == 2:
        #Muestro el inventario
        print("Bienvenido al seguimiento de stock")
        inventario.mostrar_inventario()

    elif opcion == 3:
        #Realiza acciones el personal de restaurante para marcar pedidos como preparados o listos para servir
        print("Bienvenido al apartado de la cola de pedidos")
        opcion_cola = 1
        while opcion_cola != 0:
            print("1. Marcar pedido como preparado")
            print("2. Marcar pedido como listo para servir")
            print("3. Ver la cola de pedidos")
            print("4. Busqueda secuencial")
            print("0. Salir")
            try:
                opcion_cola = int(input(""))
            except ValueError:
                print("Ingrese solo numeros")
                opcion_cola = 5
            if opcion_cola == 1:
                cola.preparar_pedido()
            elif opcion_cola == 2:
                cola.listo_para_servir()

            elif opcion_cola == 3:
                cola.mostrar_elementos_cola()

            elif opcion_cola == 4:
                num_orden = int(input("Ingrese el numero de orden a buscar: "))
                resultado = cola.busqueda_secuencial(num_orden)
                if resultado != -1:
                    print(f"El numero de orden {num_orden} está en la posición {resultado}")
                else:
                    print(f"El numero de orden {num_orden} no está en la lista")


