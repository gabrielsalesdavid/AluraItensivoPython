# Python - Fundamentos da Linguagem

## 1. Introdução ao Python

Python é uma linguagem de programação de alto nível, interpretada e dinamicamente tipada. Criada por Guido van Rossum em 1989, é conhecida por sua sintaxe clara e legível.

### Características Principais
- **Dinâmica**: Tipos definidos em tempo de execução
- **Interpretada**: Código executado linha por linha
- **Simples e Legível**: Código similar à linguagem natural
- **Multiplataforma**: Funciona em Windows, Linux, macOS
- **Extensível**: Pode ser estendida com C/C++

---

## 2. Tipos de Dados Fundamentais

### 2.1 Números Inteiros (int)
```python
numero_inteiro = 42
numero_negativo = -10
numero_grande = 1000000

# Operações
resultado = 10 + 5  # 15
resultado = 10 - 3  # 7
resultado = 10 * 3  # 30
resultado = 10 / 3  # 3.3333...
resultado = 10 // 3 # 3 (divisão inteira)
resultado = 10 % 3  # 1 (resto)
resultado = 2 ** 3  # 8 (potência)
```

### 2.2 Números Ponto Flutuante (float)
```python
numero_decimal = 3.14
numero_cientifica = 1.5e-3  # 0.0015

# Operações similares aos inteiros
resultado = 10.5 + 2.3  # 12.8
resultado = 5.0 / 2.0   # 2.5
```

### 2.3 Cadeias de Caracteres (str)
```python
texto = "Olá, Mundo!"
texto_aspas_simples = 'Python'
texto_multilinha = """
Esta é uma cadeia
de caracteres com
múltiplas linhas
"""

# Concatenação
resultado = "Olá" + " " + "Mundo"

# Repetição
resultado = "Ha" * 3  # "HaHaHa"

# Comprimento
tamanho = len("Python")  # 6

# Indexação
primeira_letra = "Python"[0]  # "P"
ultima_letra = "Python"[-1]   # "n"

# Slicing
substring = "Python"[0:3]  # "Pyt"
```

### 2.4 Valores Booleanos (bool)
```python
verdadeiro = True
falso = False

# Operações lógicas
resultado = True and False  # False
resultado = True or False   # True
resultado = not True        # False
```

### 2.5 Tipo None
```python
valor_nulo = None

# Verificação
if valor_nulo is None:
    print("Valor é nulo")
```

---

## 3. Estruturas de Dados

### 3.1 Listas (list)
Coleções ordenadas e mutáveis de elementos.

```python
lista = [1, 2, 3, 4, 5]
lista_mista = [1, "texto", 3.14, True]

# Acesso
primeiro = lista[0]      # 1
ultimo = lista[-1]       # 5

# Modificação
lista[0] = 10            # Altera elemento

# Adição
lista.append(6)          # Adiciona ao final
lista.insert(0, 0)       # Adiciona na posição

# Remoção
lista.remove(3)          # Remove o valor 3
removido = lista.pop()   # Remove o último
del lista[0]             # Deleta o primeiro

# Operações
tamanho = len(lista)
lista_ordenada = sorted(lista)
lista.reverse()          # Inverte
```

### 3.2 Tuplas (tuple)
Coleções ordenadas e imutáveis.

```python
tupla = (1, 2, 3, 4, 5)
tupla_unitaria = (1,)    # Necessário a vírgula

# Acesso similar à lista
primeiro = tupla[0]      # 1

# NÃO podem ser modificadas
# tupla[0] = 10  # Erro!

# Desempacotamento
a, b, c = (1, 2, 3)
```

### 3.3 Dicionários (dict)
Coleções de pares chave-valor.

```python
dicionario = {
    "nome": "João",
    "idade": 30,
    "cidade": "São Paulo"
}

# Acesso
nome = dicionario["nome"]        # "João"
idade = dicionario.get("idade")  # 30

# Modificação
dicionario["idade"] = 31
dicionario["profissao"] = "Engenheiro"

# Remoção
del dicionario["cidade"]
removido = dicionario.pop("profissao")

# Iteração
for chave in dicionario:
    print(chave, dicionario[chave])

for chave, valor in dicionario.items():
    print(f"{chave}: {valor}")
```

### 3.4 Conjuntos (set)
Coleções desordenadas sem duplicatas.

```python
conjunto = {1, 2, 3, 4, 5}
conjunto_vazio = set()  # Não usar {}

# Operações
conjunto.add(6)
conjunto.remove(3)

# Operações de conjunto
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

uniao = conjunto1 | conjunto2        # {1, 2, 3, 4, 5}
intersecao = conjunto1 & conjunto2   # {3}
diferenca = conjunto1 - conjunto2    # {1, 2}
```

---

## 4. Variáveis e Escopo

### 4.1 Nomenclatura
```python
# Válidos
variavel_valida = 10
_variavel_privada = 20
variavel123 = 30

# Inválidos
# 123variavel = 10  # Não pode começar com número
# variavel-invalida = 10  # Não pode ter hífen
```

### 4.2 Escopo de Variáveis
```python
variavel_global = 10  # Escopo global

def funcao():
    variavel_local = 20       # Escopo local
    global variavel_global    # Acessa global
    
    print(variavel_global)
    print(variavel_local)

print(variavel_global)
# print(variavel_local)  # Erro - não existe aqui
```

---

## 5. Operadores

### 5.1 Operadores Aritméticos
```python
a = 10
b = 3

print(a + b)   # 13 (adição)
print(a - b)   # 7  (subtração)
print(a * b)   # 30 (multiplicação)
print(a / b)   # 3.333... (divisão)
print(a // b)  # 3  (divisão inteira)
print(a % b)   # 1  (módulo/resto)
print(a ** b)  # 1000 (potência)
```

### 5.2 Operadores de Comparação
```python
a = 10
b = 5

print(a == b)  # False (igual)
print(a != b)  # True  (diferente)
print(a > b)   # True  (maior)
print(a < b)   # False (menor)
print(a >= b)  # True  (maior ou igual)
print(a <= b)  # False (menor ou igual)
```

### 5.3 Operadores Lógicos
```python
a = True
b = False

print(a and b)  # False
print(a or b)   # True
print(not a)    # False
```

### 5.4 Operadores de Atribuição
```python
x = 10
x += 5   # x = x + 5 = 15
x -= 3   # x = x - 3 = 12
x *= 2   # x = x * 2 = 24
x /= 4   # x = x / 4 = 6.0
x //= 2  # x = x // 2 = 3.0
x **= 2  # x = x ** 2 = 9.0
x %= 2   # x = x % 2 = 1.0
```

---

## 6. Controle de Fluxo

### 6.1 Condicional if/elif/else
```python
idade = 18

if idade < 13:
    print("Criança")
elif idade < 18:
    print("Adolescente")
else:
    print("Adulto")

# Condicional ternária
resultado = "Adulto" if idade >= 18 else "Menor"
```

### 6.2 Loops com while
```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1

# Interrupção
while True:
    entrada = input("Digite 'sair' para sair: ")
    if entrada == "sair":
        break
```

### 6.3 Loops com for
```python
# Iteração sobre lista
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    print(numero)

# Com range
for i in range(5):      # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):   # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
    print(i)

# Enumeração
for indice, valor in enumerate([10, 20, 30]):
    print(f"{indice}: {valor}")

# Iteração sobre dicionário
dicionario = {"a": 1, "b": 2}
for chave, valor in dicionario.items():
    print(f"{chave}: {valor}")
```

### 6.4 Controle de Loops
```python
# break - interrompe o loop
for i in range(10):
    if i == 5:
        break
    print(i)  # 0, 1, 2, 3, 4

# continue - pula para próxima iteração
for i in range(5):
    if i == 2:
        continue
    print(i)  # 0, 1, 3, 4
```

---

## 7. Funções

### 7.1 Definição Básica
```python
def saudacao(nome):
    """Função que saudação uma pessoa"""
    print(f"Olá, {nome}!")

saudacao("João")  # Olá, João!
```

### 7.2 Retorno de Valores
```python
def somar(a, b):
    return a + b

resultado = somar(5, 3)  # 8
```

### 7.3 Parâmetros Padrão
```python
def potencia(base, expoente=2):
    return base ** expoente

print(potencia(5))      # 25
print(potencia(5, 3))   # 125
```

### 7.4 Argumentos Variáveis
```python
# *args - argumentos posicionais
def somar_numeros(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

print(somar_numeros(1, 2, 3, 4, 5))  # 15

# **kwargs - argumentos nomeados
def criar_pessoa(**info):
    print(info)

criar_pessoa(nome="João", idade=30, cidade="São Paulo")
# {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo'}
```

### 7.5 Argumentos Nomeados
```python
def criar_arquivo(nome, extensao=".txt", diretorio="."):
    return f"{diretorio}/{nome}{extensao}"

resultado = criar_arquivo("documento", extensao=".pdf", diretorio="/home")
```

---

## 8. Manipulação de Strings

### 8.1 Métodos de String
```python
texto = "  Olá, Mundo!  "

print(texto.strip())          # "Olá, Mundo!"
print(texto.upper())          # "  OLÁ, MUNDO!  "
print(texto.lower())          # "  olá, mundo!  "
print(texto.replace("Mundo", "Python"))  # "  Olá, Python!  "

palavras = texto.split(",")   # ['  Olá', ' Mundo!  ']
resultado = "-".join(["a", "b", "c"])  # "a-b-c"

print(texto.startswith("Olá"))     # False (por causa dos espaços)
print("Mundo" in texto)            # True
```

### 8.2 Formatação
```python
nome = "João"
idade = 30

# Concatenação
resultado = "Nome: " + nome + ", Idade: " + str(idade)

# .format()
resultado = "Nome: {}, Idade: {}".format(nome, idade)
resultado = "Nome: {0}, Idade: {1}".format(nome, idade)
resultado = "Nome: {n}, Idade: {i}".format(n=nome, i=idade)

# f-strings (Python 3.6+)
resultado = f"Nome: {nome}, Idade: {idade}"
resultado = f"Próximo ano: {idade + 1}"
```

### 8.3 Indexação e Slicing
```python
texto = "Python"

print(texto[0])       # "P" (primeira letra)
print(texto[-1])      # "n" (última letra)
print(texto[0:2])     # "Py"
print(texto[2:])      # "thon"
print(texto[:3])      # "Pyt"
print(texto[::2])     # "Pto" (cada 2º caractere)
print(texto[::-1])    # "nohtyP" (reverso)
```

---

## 9. Tratamento de Erros

### 9.1 Try/Except
```python
try:
    numero = int("abc")  # Erro!
except ValueError:
    print("Erro: Valor inválido")

try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Erro: Divisão por zero")
```

### 9.2 Múltiplas Exceções
```python
try:
    # Código
    pass
except ValueError:
    print("Erro de valor")
except (TypeError, IndexError):
    print("Erro de tipo ou índice")
except Exception as e:
    print(f"Erro geral: {e}")
```

### 9.3 Finally
```python
try:
    arquivo = open("dados.txt", "r")
    conteudo = arquivo.read()
except FileNotFoundError:
    print("Arquivo não encontrado")
finally:
    arquivo.close()  # Sempre executa
```

---

## 10. Entrada e Saída

### 10.1 Leitura de Entrada
```python
# input() retorna sempre string
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
```

### 10.2 Saída com print
```python
print("Olá")
print("A", "B", "C")  # Separados por espaço
print("A", "B", sep="-")  # A-B
print("A", end="")  # Sem quebra de linha

# Múltiplos valores
print(f"Nome: {nome}, Idade: {idade}")
```

### 10.3 Manipulação de Arquivos
```python
# Leitura
with open("arquivo.txt", "r") as arquivo:
    conteudo = arquivo.read()          # Todo conteúdo
    linhas = arquivo.readlines()       # Lista de linhas

# Escrita
with open("arquivo.txt", "w") as arquivo:
    arquivo.write("Novo conteúdo\n")
    arquivo.writelines(["Linha 1\n", "Linha 2\n"])

# Anexação
with open("arquivo.txt", "a") as arquivo:
    arquivo.write("Mais conteúdo\n")
```

---

## 11. Boas Práticas

### 11.1 Nomenclatura (PEP 8)
```python
# Variáveis e funções: snake_case
minha_variavel = 10
def minha_funcao():
    pass

# Classes: PascalCase
class MinhaClasse:
    pass

# Constantes: UPPER_CASE
CONSTANTE = 100
```

### 11.2 Comentários
```python
# Comentário de linha única

"""
Comentário de múltiplas linhas
ou docstring para funções
"""

def funcao():
    """Descrição breve da função"""
    pass
```

### 11.3 Boas Práticas Gerais
- Use nomes descritivos
- Evite variáveis de uma letra (exceto em loops)
- Função pequena = função boa
- DRY: Don't Repeat Yourself
- KISS: Keep It Simple, Stupid
- Sempre use context managers (`with`)

---

## Conclusão

Os fundamentos apresentados constituem a base para qualquer programa Python. Dominar estes conceitos é essencial antes de avançar para tópicos mais complexos como Programação Orientada a Objetos e bibliotecas especializadas.
