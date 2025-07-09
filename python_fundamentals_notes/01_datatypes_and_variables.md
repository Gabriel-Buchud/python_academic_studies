# 🐍 Estudos em Python - Gabriel Buchud

## 📘 Parte 1 – Fundamentos

> **Resumo:** Nesta parte vamos ver os tipos de dados básicos, criação de variáveis e como o Python lida com a atribuição de valores. Tentarei explicar de forma simples e acessível.

---

### 🧠 1. Tipos de Dados

Uma das primeiras coisas que você precisa entender em Python são os **tipos de dados**.

Python é uma linguagem **dinamicamente tipada**, o que significa que você não precisa dizer qual é o tipo de uma variável, ele adivinha sozinho com base no que você colocou lá dentro.

Mas vamos com calma! Mesmo que ele adivinhe, **você precisa entender o que está acontecendo com seu programa** pra não escrever código confuso ou cometer erros bobos.

#### 🔹 Tipos principais de dados que você vai ver o tempo todo:

| Tipo       | Exemplo         | O que representa                       |
|------------|-----------------|----------------------------------------|
| `int`      | `5`, `-10`      | Números inteiros                       |
| `float`    | `3.14`, `-0.01` | Números com casas decimais             |
| `str`      | `"texto"`       | Sequência de caracteres (string)       |
| `bool`     | `True`, `False` | Verdadeiro ou falso (lógica)           |
| `list`     | `[1, 2, 3]`     | Lista mutável (você pode mexer nela)   |
| `tuple`    | `(1, 2)`        | Lista imutável (não dá pra mudar)      |
| `dict`     | `{"a": 1}`      | Dicionário (chave → valor)             |
| `set`      | `{1, 2, 3}`     | Conjunto sem valores repetidos         |
| `NoneType` | `None`          | “Nada aqui”, tipo o vazio do vazio     |

```python
# Exemplos de tipos em ação
idade       = 25                 # int
altura      = 1.75               # float
nome        = "Gabriel"          # str
ativo       = True               # bool
lista       = [1, 2, 3]          # list
coordenadas = (10, 20)           # tuple
pessoa      = {"nome": "Ana"}    # dict
unicos      = {1, 2, 2, 3}       # set → vira {1, 2, 3}
vazio       = None               # NoneType
```

#### 💡 Dica: use `type()` para verificar o tipo de uma variável

Essa dica é bem útil em códigos maiores ou quando você está mexendo em um projeto que já existia e precisa entender o que cada variável carrega.

```python
print(type(25))                              # int
print(type(1.75))                            # float
print(type("Gabriel"))                       # str
print(type(True))                            # bool
print(type(["maçã", "banana", "uva"]))       # list
print(type((10.5, -23.4)))                   # tuple
print(type({12, 23, 45}))                    # set
print(type({"nome": "Maria", "idade": 30}))  # dict
print(type(None))                            # NoneType
```

🧪 *"Mas pra que saber isso?"*  
Pra você entender o que pode (ou não) fazer com aquela variável.  
Outro exemplo: não dá pra somar string com número direto, tem que converter antes.

---

### ✍️ 2. Variáveis

Variáveis são **nomes que damos a valores** pra guardar informações e usar depois.

Pensa como se fossem **caixinhas com etiquetas**. Você dá um nome pra cada caixinha e bota algo lá dentro.

```python
nome = "Gabriel"  # etiqueta: nome / conteúdo: "Gabriel"
ano  = 2025       # etiqueta: ano  / conteúdo: 2025
```

Toda vez que você escreve `nome`, o Python entende que é pra olhar dentro daquela caixinha.

💡 **Importante:** o sinal de igual `=` em Python **não significa "igualdade"**, como na matemática. Aqui ele tem o valor semântico de **"recebe"**.

```python
x = 10  # Leia como "x recebe 10"
```

---

#### 🔸 Boas práticas (pra não se perder depois):

- ✅ Use nomes **descritivos**: `nome_completo`, `valor_total`
- ✅ Use **snake_case** (minúsculas com underline)
- ❌ Evite nomes genéricos como `x1`, `coisa`, `abc`
- ❌ Nunca comece com número
- ❌ Não use espaços, acentos ou `ç`
- ❌ Não use palavras reservadas como `if`, `class`, `while`

```python
# Correto
velocidade_media = 90

# Errado (mas funciona, só é ruim)
VM = 90
```

🧠 *"Mas e se eu só quiser testar rapidinho?"*  
Pode usar nomes simples (`a`, `b`, `x`) enquanto estiver aprendendo, mas tente melhorar os nomes assim que puder.

💡 **Por que seguir um padrão é importante?**  
Ter um padrão ajuda seu código a ser mais **legível**, **organizado** e **fácil de manter**.

O padrão mais usado em Python é o **snake_case**:

```python
nome_completo = "João da Silva"  # tudo minúsculo e separado por underline
```

---

### ✨ Dicas extras que você já pode usar

```python
x, y, z = 1, 2, 3     # atribuição múltipla
a = b = c = 0         # todos recebem 0
a, b = b, a           # troca de valores entre variáveis
```

---

Essa foi a base.  
Com isso você já consegue declarar, armazenar e inspecionar valores com segurança.  
Bora pra Parte 2!