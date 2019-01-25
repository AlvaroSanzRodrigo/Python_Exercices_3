def lista_de_personas_formateada(lista_de_personas):
    lista_de_personas_formateada_v = []
    for persona in lista_de_personas:
        lista_de_personas_formateada_v.append("" + persona[0] + ", " + persona[2] + "., " + persona[1])
    print(lista_de_personas_formateada_v)


lista_de_personas_formateada([("Alberto", "Ruiz", "A"), ("Jose", "Garcia", "J"), ("Carlos","Perez", "C"), ("Jorge", "Vázquez", "J"), ("Sebastian", "Tangarife", "S")])
