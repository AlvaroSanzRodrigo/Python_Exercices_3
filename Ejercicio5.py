def buscar_en_agenda(cadena, lista_de_contactos):
    for contacto in lista_de_contactos:
        if not contacto[0].find(cadena) == -1 or not contacto[1].find(cadena) == -1:
            print(contacto)


buscar_en_agenda("n", [("Ana", "Ruiz", "6666666666"), ("Silvia", "Perez", "999999999"), ("Iigo", "Reyes", "888888888"), ("Carlos", "Mancebo", "666555444")])
