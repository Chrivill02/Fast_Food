Encabezados="Nombre;NIT;Numero de Telefono; Direccion, Compras"
Clientes={}
Condition=False

while not Condition:
    print("Pedido en proceso")
    cliente=input("Ingrese el NIT del cliente: ")
    if cliente not in Clientes:
        print("Nuevo cliente")
        nombre=input("Ingrese el nombre del nuevo cliente: ")
        direccion=input("Ingrese la dirección del nuevo cliente: ")
        telefono=input("Ingrese el número de teléfono del nuevo cliente: ")
        Compras=0
        Clientes[cliente]={"Nombre":nombre,"Direccion":direccion,"Telefono":telefono,"Compras":Compras}
    else:
        informacion = Clientes[cliente]
        print("Cliente:", informacion["Nombre"])
        print("Numero de contacto:", informacion["Telefono"])
        print("Direccion:", informacion["Direccion"])
        opcion=input("La informacion es correcta? presione 1 para confirmar y 2 para modificar: ")
        if opcion == "1":
            print("Pedido en camino")
            Compras_Realizadas = informacion["Compras"]
            Compras_Realizadas += 1
            Clientes[cliente]["Compras"] = Compras_Realizadas
            if Compras_Realizadas>=50:
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
                Nuevo=input("Ingrese el Nombre: ")
                Clientes[cliente]["Numero de telefono"]=Nuevo
            elif opcion2=="3":
                Nuevo=input("Ingrese el Nombre: ")
                Clientes[cliente]["Direccion"]=Nuevo
            else:
                print("Por favor seleccione una opcion valida")
        else:
            print("Por favor ingrese una opcion valida")