""" Existe un número entero positivo de 4 dígitos que presenta las siguientes características:
  
    1.  La suma de sus 4 dígitos es 16.
    2.  El primer dígito es un número par.
    3.  El segundo dígito es un múmero primo.
    4.  El cuarto dígito es la tercera parte del primer dígito.
  
"""


def suma_digitos(lista):
    suma = 0
    for l in lista:
        suma += l
    return suma


def es_par(numero):
    if (numero % 2) == 0:
        return True
    else:
        return False


def es_primo(numero):
    if numero < 1:
        return False
    elif numero == 2:
        return True
    else:
        for n in range(2, numero):
            if numero % n == 0:
                return False
        return True


def n4_tercera_parte_n1(n1, n4):
    if n1 == 3 * n4:
        return True
    else:
        return False


for num in range(1000, 10000, 1):
#num = 4444
    digitos = [int(n) for n in str(num)]
#print(digitos, suma_digitos(digitos))
    if suma_digitos(digitos) == 16:
        if es_par(digitos[0]):
            if es_primo(digitos[1]):
                if n4_tercera_parte_n1(digitos[0], digitos[3]):
                    print(num)
                    break
