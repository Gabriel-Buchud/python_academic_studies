"""
Enunciado:
Desenvolva um programa em Python para calcular o preço do ingresso de um cinema
conforme a idade do cliente. As regras de cobrança são as seguintes:

- Menores de 3 anos não pagam ingresso.
- Pessoas com idade entre 3 e 12 anos pagam R$15,00.
- Pessoas com mais de 12 anos pagam R$30,00.

O programa deve solicitar a idade de vários clientes em sequência.
Quando o usuário digitar 0, o programa deve encerrar o laço e apresentar:

- O total de pessoas que compraram ingresso
- O total de dinheiro arrecadado
- A média de idade de todas as pessoas que compraram ingresso

Autor: Gabriel
Data: 30/06/2025
Instituição: Uninter
"""

pessoas = 0
dinheiro = 0
soma_idades = 0

while True:
    try:
        idade = int(input("Digite a idade do cliente (0 para encerrar): "))
    except ValueError:
        print("Entrada inválida! Digite um número inteiro.")
        continue

    if idade == 0:
        break

    if idade < 3:
        ingresso = 0
    elif idade > 12:
        ingresso = 30
    else:
        ingresso = 15

    dinheiro += ingresso
    pessoas += 1
    soma_idades += idade

    print(f"Ingresso: R${ingresso:.2f}\n")

if pessoas > 0:
    media_idade = soma_idades / pessoas
    print("===== RESUMO =====")
    print(f"Total de pessoas: {pessoas}")
    print(f"Total arrecadado: R${dinheiro:.2f}")
    print(f"Média de idade: {media_idade:.2f}")
else:
    print("Nenhum ingresso foi vendido.")
