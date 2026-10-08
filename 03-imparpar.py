def impar():

    quantidade = int(input("Digite a quantidade de números ímpares: "))
    valor_inicial = -1
    contador = 1

    while contador <= quantidade:
        valor_inicial += 2
        print(valor_inicial)
        contador += 1

def par():

    quantidade = int(input("Digite a quantidade de números pares: "))
    valor_inicial = 0
    contador = 1

    while contador <= quantidade:
        valor_inicial += 2
        print(valor_inicial)
        contador += 1

while True:
    print("Ímpar ou Par")
    print("1- Impár")
    print("2- Par")

    opcao = input ("Escolha uma opção: ")

    if opcao == "1":
        impar()


    if opcao == "2":
        par()