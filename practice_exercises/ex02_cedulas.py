"""
Enunciado:
Escreva um programa em Python que leia um valor inteiro fornecido pelo usuário
e calcule a quantidade mínima de cédulas necessárias para representar este valor,
considerando as seguintes cédulas disponíveis: 100, 50, 20, 10, 5 e 1 reais.

Autor: Gabriel
Data: 30/06/2025
Instituição: Uninter
"""

while True:
    # entrada e validação do valor
    while True:
        try:
            valor = int(input("Digite um valor inteiro positivo: "))
            if valor <= 0:
                print("Valor inválido! Digite um número maior que zero.")
            else:
                break
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.")

    original = valor

    # variáveis para guardar quantidade de cédulas
    qtd_100 = 0
    qtd_50 = 0
    qtd_20 = 0
    qtd_10 = 0
    qtd_5 = 0
    qtd_1 = 0

    # cálculo das cédulas
    if valor >= 100:
        qtd_100 = valor // 100
        valor -= qtd_100 * 100

    if valor >= 50:
        qtd_50 = valor // 50
        valor -= qtd_50 * 50

    if valor >= 20:
        qtd_20 = valor // 20
        valor -= qtd_20 * 20

    if valor >= 10:
        qtd_10 = valor // 10
        valor -= qtd_10 * 10

    if valor >= 5:
        qtd_5 = valor // 5
        valor -= qtd_5 * 5

    if valor >= 1:
        qtd_1 = valor
        valor = 0

    print("\n===== RESUMO DA OPERAÇÃO =====")

    print(f"Valor total: R$ {original}")
    if qtd_100 > 0:
        print(f"Cédulas de 100: {qtd_100}")
    if qtd_50 > 0:
        print(f"Cédulas de 50: {qtd_50}")
    if qtd_20 > 0:
        print(f"Cédulas de 20: {qtd_20}")
    if qtd_10 > 0:
        print(f"Cédulas de 10: {qtd_10}")
    if qtd_5 > 0:
        print(f"Cédulas de 5: {qtd_5}")
    if qtd_1 > 0:
        print(f"Cédulas de 1: {qtd_1}")

    print("=============================\n")

    # pergunta se quer continuar
    continuar = input("Deseja calcular outro valor? (s/n): ").lower()
    if continuar != 's':
        print("Programa encerrado. Obrigado!")
        break
