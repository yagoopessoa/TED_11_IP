import random

# Parte 1: Leitura de 10 números e verificação de repetidos
def verificar_repetidos():
    VET = []
    for i in range(10):
        num = int(input(f"Digite o número {i+1}: "))
        VET.append(num)

    repetidos = {}
    for i, num in enumerate(VET):
        if num in repetidos:
            repetidos[num].append(i)
        else:
            repetidos[num] = [i]

    print("\nNúmeros repetidos e suas posições:")
    for num, posicoes in repetidos.items():
        if len(posicoes) > 1:
            print(f"Número {num} encontrado nas posições: {posicoes}")

# Parte 2: Criação e manipulação da matriz
def manipular_matriz():
    # Criação da matriz A 10x10 com valores aleatórios
    A = [[random.randint(0, 10) for _ in range(10)] for _ in range(10)]

    # Impressão da matriz A
    print("\nMatriz A:")
    for linha in A:
        print(linha)

    # Cálculo da soma de todos os valores da matriz A
    soma = sum(sum(linha) for linha in A)
    print(f"\nSoma de todos os valores da matriz A: {soma}")

    # Criação da matriz B
    B = [[valor * 3 for valor in linha] for linha in A]

    # Impressão da matriz B
    print("\nMatriz B (cada elemento de A * 3):")
    for linha in B:
        print(linha)

# Execução das funções
verificar_repetidos()
manipular_matriz()
