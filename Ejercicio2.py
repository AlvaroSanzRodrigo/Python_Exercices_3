def es_subcadena(cadena, subcadena):
    if cadena.find(subcadena) == -1:
        print("no es subcadena")
    else:
        print("es subcadena")


def cual_va_primero(cadena_a, cadena_b):
    if cadena_a < cadena_b:
        print(cadena_a)
    else:
        print(cadena_b)


es_subcadena("Pepelu", "lu")
cual_va_primero("B", "A")
