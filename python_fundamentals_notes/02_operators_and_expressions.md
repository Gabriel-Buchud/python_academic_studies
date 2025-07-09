# 🐍 Estudos em Python - Gabriel Buchud

## 📘 Parte 2 – `in`, Operadores Aritméticos, Relacionais e Lógicos

> **Resumo:** Aqui vamos entender como funciona o operador `in`, que verifica se algo existe dentro de algo. Também vamos explorar os operadores aritméticos (contas básicas) e os operadores relacionais (comparações).

---

### 🔍 3. O operador `in`

O `in` serve pra **verificar se algo está dentro de outra coisa**.  
Funciona com strings, listas, tuplas, dicionários e sets.

```python
frutas = ["maçã", "banana", "uva"]

print("banana" in frutas)   # True (banana está na lista)
print("melancia" in frutas) # False (melancia não está)
```

🧠 Pense assim: a lista `frutas` é como uma cesta.  
O `in` pergunta: **“Essa fruta está na cesta?”**  
E responde com `True` ou `False`.

Com strings, o `in` verifica se um pedaço de texto está dentro de outro:

```python
mensagem = "Olá, Gabriel!"

print("Gabriel" in mensagem)  # True
print("Python" in mensagem)   # False
```

📦 Aqui, `mensagem` é como um bilhete. O `in` procura uma palavra nesse bilhete.

Com dicionários, o `in` verifica se uma **chave** existe (não os valores!):

```python
dados = {"nome": "Ana", "idade": 30}

print("nome" in dados)   # True  → chave existe
print("Ana" in dados)    # False → valor, não chave
print(30 in dados)       # False → idem
```

🧠 Lembre-se: ele procura apenas as **chaves**. Valores são ignorados nesse caso.

---

### 💡 Dica prática com `in`

```python
frutas = ["maçã", "banana", "uva"]

if "pera" not in frutas:
    frutas.append("pera")
```

📌 Verifica se "pera" não está na lista antes de adicionar. Isso evita duplicatas.

---

### ➕ 4. Operadores Aritméticos

São os operadores matemáticos que você já conhece:

```python
a = 10
b = 3

print(a + b)   # 13 → adição
print(a - b)   # 7  → subtração
print(a * b)   # 30 → multiplicação
print(a / b)   # 3.33... → divisão normal
print(a // b)  # 3  → divisão inteira (sem casas decimais)
print(a % b)   # 1  → resto da divisão
print(a ** b)  # 1000 → potência (10³)
```

💬 *“Mas quando eu usaria isso?”*  
Exemplo: saber se um número é par ou ímpar com `%`:

```python
numero = 7

print(numero % 2 == 0)  # False → 7 é ímpar
```

---

### ⚖️ 5. Operadores Relacionais

Comparações que retornam `True` ou `False`. Servem pra saber se algo é maior, menor, igual, etc.

```python
x = 10
y = 5

print(x == y)   # False → é igual?
print(x != y)   # True  → é diferente?
print(x > y)    # True  → é maior?
print(x < y)    # False → é menor?
print(x >= 10)  # True  → maior ou igual?
print(y <= 5)   # True  → menor ou igual?
```

| Operador | Significado        | Exemplo   | Resultado |
|----------|--------------------|-----------|-----------|
| `==`     | Igual a            | x == y    | False     |
| `!=`     | Diferente de       | x != y    | True      |
| `>`      | Maior que          | x > y     | True      |
| `<`      | Menor que          | x < y     | False     |
| `>=`     | Maior ou igual a   | x >= 10   | True      |
| `<=`     | Menor ou igual a   | y <= 5    | True      |

Você também pode guardar o resultado em uma variável:

```python
maior_de_idade = 20 >= 18
print(maior_de_idade)  # True
```

---

### 🔢 6. Tabela Verdade (operadores lógicos)

Será mais usada na Parte 3, mas aqui vai um gostinho:

| A       | B       | `A and B` | `A or B` |
|---------|---------|-----------|----------|
| True    | True    | True      | True     |
| True    | False   | False     | True     |
| False   | True    | False     | True     |
| False   | False   | False     | False    |

🧠 Interprete assim:

- `and` → só dá `True` se **ambos forem verdadeiros**
- `or` → dá `True` se **pelo menos um** for verdadeiro

---

✅ Com tudo isso, você já consegue fazer verificações, entender valores e preparar o caminho para **condições e laços de repetição**, tema da próxima parte.
