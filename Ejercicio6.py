agenda = {'claudio': '916300512', 'aurelio': '612312312', 'pedro': '987987987'}

busqueda = input("Introduce nombre: ")
while busqueda != "*":
    if busqueda in agenda:
        print("Ya existe, el numero de telefono es " + agenda.get(busqueda))
        if input("¿deseas modificarlo? s/n") == "s":
            agenda.update({busqueda: input("telefono modificado: ")})
    else:
        if input("¿deseas agregar, " + busqueda +"? s/n") == "s":
            agenda.update({busqueda: input("telefono: ")})
    busqueda = input("Introduce nombre: ")

