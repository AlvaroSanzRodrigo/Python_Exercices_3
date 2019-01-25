def separar(cadena, caracter_separador):
    cadena_separada = ""
    for i in range(0, len(cadena)):
        cadena_separada += cadena[i] + caracter_separador
    print(cadena_separada)


def cambia_espacios(cadena, caracter):
    cadena_cambiada = cadena.replace(" ", caracter)
    print(cadena_cambiada)


def reemplazar_digitos(cadena, caracter):
    for i in range(10):
        cadena = cadena.replace(str(i), caracter)
    print(cadena)


def insertar_cada_3_digitos(cadena, caracter):
    contador = 0
    cadena_cambiada = ""
    for caracter_de_cadena in cadena:
        if contador != 0 and contador % 3 == 0:
            cadena_cambiada = cadena_cambiada + caracter
        cadena_cambiada += caracter_de_cadena
        contador = contador + 1
    print(cadena_cambiada)


separar("hola", ",")
cambia_espacios("Hola que tal", "_")
reemplazar_digitos("hola 1234567890", "x")
insertar_cada_3_digitos("2552552550", ".")
