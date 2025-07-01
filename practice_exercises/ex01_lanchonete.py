
"""
Enunciado:
Crie um programa que mostre na tela 5 produtos a serem comprados e
simule pedidos de uma lanchonete, permitindo escolher os produtos,
calcular o valor total e exibir o resumo do pedido.

Autor: Gabriel
Data: 30/06/2025
Instituição: Uninter
"""

# mostrar o menu
print("===================================")
print(" LANCHONETE - MENU")
print("===================================")
print("01 - COXINHA R$ 5,00")
print("02 - PASTEL R$ 7,00")
print("03 - CAFÉ R$ 4,00")
print("04 - SUCO NATURAL R$ 6,00")
print("05 - BOLO DE CENOURA R$ 8,00")
print("06 - SAIR")
print("===================================")

total = 0
subtotal = 0
compras = []

# ler a opção
while True:
    op = int(input("Digite o número do produto: "))
    if op == 6:
        break

    qtd = int(input("Digite a quantidade de produtos: "))

    # calcular o total e  subtotal
    if op == 1:
        subtotal = qtd * 5.00
        compras.append(("Coxinha", qtd, subtotal))
        total += subtotal
    elif op == 2:
        subtotal = qtd * 7.00
        compras.append(("Pastel", qtd, subtotal))
        total += subtotal
    elif op == 3:
        subtotal = qtd * 4.00
        compras.append(("Café", qtd, subtotal))
        total += subtotal
    elif op == 4:
        subtotal = qtd * 6.00
        compras.append(("Suco Natural", qtd, subtotal))
        total += subtotal
    elif op == 5:
        subtotal = qtd * 8.00
        compras.append(("Bolo de Cenoura", qtd, subtotal))
        total += subtotal
    else:
        print("Produto não encontrado!, tente novamente.")

print("\nResumo do pedido:\n")
for nome, quantidade, subtotal in compras:
    print(f"{quantidade}x {nome} - R$ {subtotal:.2f}")

print(f"\nO valor total da compra foi de R$ {total:.2f}")
