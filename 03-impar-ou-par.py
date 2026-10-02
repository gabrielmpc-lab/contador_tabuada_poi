tipo = input("Escolha Par ou Ímpar: ")
quantidade = int(input("Quantos números você quer ver: "))

contador = 0
numero = 1

while contador < quantidade:
    if tipo == "par" or tipo == "pares":
        if numero % 2 == 0:
            print(numero)
            contador += 1

    elif tipo == "impares" or tipo == "impar" or tipo == "ímpar" or tipo == "ímpares":
        if numero % 2 != 0:
            print(numero)
            contador += 1

    numero +=1