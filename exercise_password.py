def password():
    """
    Ejercicio 10 - Validador de Contraseña

    Leer una contraseña mediante input(). Validar que cumpla con los siguientes requisitos:
    1. Debe tener al menos 8 caracteres de longitud
    2. Debe contener al menos un número (usar el operador in para verificar cada dígito del 0 al 9)

    Si cumple ambos requisitos, imprimir "Contraseña valida".
    Si no cumple, imprimir cuál requisito falta.

    Ejemplo:
        Para la entrada "abc12345", la salida esperada es:
        Contraseña valida

        Para la entrada "abc123", la salida esperada es:
        Contraseña muy corta

        Para la entrada "abcdefgh", la salida esperada es:
        Debe contener un numero

        Para la entrada "abc", la salida esperada es:
        Contraseña muy corta
        Debe contener un numero
    """

    contrasenA = str(input())

    tieneDigito = ("0" in contrasenA or "1" in contrasenA or "2" in contrasenA or "3" in contrasenA or "4" in contrasenA or "5" in contrasenA or "6" in contrasenA or "7" in contrasenA or "8" in contrasenA or "9" in contrasenA)
    esLarga = len(contrasenA) >= 8

    if tieneDigito and esLarga:
        print("Contraseña valida")
    else:
        if not esLarga:
            print("Contraseña muy corta")
        if not tieneDigito:
            print("Debe contener un numero")
    pass
