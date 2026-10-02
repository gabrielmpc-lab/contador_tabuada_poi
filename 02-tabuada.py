numero = int(input("Digite um número: "))
vezes_multiplicando = int(input("Quantas vezes você quer multiplicar este número? "))
contador = 1

#Enquanto o contador for maior ou igual às
while (contador <= vezes_multiplicando):
    resultado = (numero * vezes_multiplicando)
    print (f"{numero} X {contador} = {resultado}")
    contador = contador + 1