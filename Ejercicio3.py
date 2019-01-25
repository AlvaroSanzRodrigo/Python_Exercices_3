def propaganda_politica(lista_de_posibles_votantes):
    for posible_votante in lista_de_posibles_votantes:
        print("Estimado " + posible_votante + ", vote por mí.")


def propaganda_politica_selectiva(lista_de_posibles_votantes, p, n):
    for posible_votante in lista_de_posibles_votantes[p:n]:
        print("Estimado " + posible_votante + ", vote por mí.")


def propaganda_politica_de_genero_binario(lista_de_posibles_votantes_o_votantas):
    for posible_votante_o_votanta in lista_de_posibles_votantes_o_votantas:
        if posible_votante_o_votanta[1] == "f":
            print("Estimada " + posible_votante_o_votanta[0] + ", vote por mí.")
        else:
            print("Estimado " + posible_votante_o_votanta[0] + ", vote por mí.")


def propaganda_politica_selectiva_de_genero_binario(lista_de_posibles_votantes_o_votantas, p, n):
    for posible_votante_o_votanta in lista_de_posibles_votantes_o_votantas[p:n]:
        if posible_votante_o_votanta[1] == "f":
            print("Estimada " + posible_votante_o_votanta[0] + ", vote por mí.")
        else:
            print("Estimado " + posible_votante_o_votanta[0] + ", vote por mí.")


propaganda_politica(("Pepe", "Luis", "Jose"))
propaganda_politica_selectiva(("Pepe", "Luis", "Jose", "Aurelio", "Sebastián", "Tomás"), 2, 5)
propaganda_politica_de_genero_binario((("Ana", "f"), ("Silvia", "f"), ("Iñigo", "m"), ("Carlos", "m")))
propaganda_politica_selectiva_de_genero_binario((("Ana", "f"), ("Silvia", "f"), ("Iñigo", "m"), ("Carlos", "m")), 0, 2)
