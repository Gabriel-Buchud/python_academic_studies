"""
Enunciado:
Desenvolva um programa em Python que utilize duas funções:

- Uma função que calcule o fatorial de um número recebido
como parâmetro, retornando o resultado do cálculo.

- Outra função que valide a entrada de dados, aceitando
apenas números inteiros positivos.

Além disso, documente a função de cálculo do fatorial
utilizando docstring (help) para que outros usuários
possam entender claramente seu funcionamento.

Autor: Gabriel
Data: 01/07/2025
Instituição: Uninter
"""

def validar_entrada():
    """
    Solicita ao usuário um número inteiro positivo (ou zero para sair)
    e garante que a entrada seja válida.
    Retorna o número digitado.
    """
    while True:
        try:
            n = int(input("Digite um número inteiro positivo (0 para encerrar): "))
            if n == 0:
                return 0
            elif n > 0:
                return n
            else:
                print("Número inválido! Digite apenas valores positivos ou zero para sair.")
        except (ValueError, TypeError):
            print("Entrada inválida! Digite apenas números inteiros.")

def fatorial(num):
    """
    Calcula o fatorial de um número inteiro positivo.
    Recebe um número como parâmetro e retorna seu fatorial.
    """
    fat = 1
    for i in range(1, num + 1):
        fat *= i
    return fat

# programa principal
while True:
    numero = validar_entrada()
    if numero == 0:
        print("Encerrando o programa.")
        break
    resultado = fatorial(numero)
    print(f"O fatorial de {numero} é {resultado}\n")
