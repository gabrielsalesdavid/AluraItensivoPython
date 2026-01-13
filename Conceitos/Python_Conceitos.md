# Python - Conceitos Avançados da Linguagem

## 1. Programação Orientada a Objetos (POO)

### 1.1 Classes e Objetos
A POO organiza código em torno de objetos que contêm dados (atributos) e comportamentos (métodos).

```python
class Pessoa:
    """Classe que representa uma pessoa"""
    
    def __init__(self, nome, idade):
        """Construtor da classe"""
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        """Método que retorna uma apresentação"""
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos"
    
    def fazer_aniversario(self):
        """Incrementa a idade"""
        self.idade += 1

# Criando instâncias
pessoa1 = Pessoa("João", 30)
pessoa2 = Pessoa("Maria", 25)

print(pessoa1.apresentar())  # Olá, meu nome é João e tenho 30 anos
pessoa1.fazer_aniversario()
print(pessoa1.idade)  # 31
```

### 1.2 Herança
Permite que uma classe herde atributos e métodos de outra.

```python
class Animal:
    """Classe base"""
    def __init__(self, nome):
        self.nome = nome
    
    def fazer_som(self):
        return "Som genérico"

class Cachorro(Animal):
    """Classe derivada"""
    def fazer_som(self):
        return "Au au!"
    
    def buscar(self, objeto):
        return f"{self.nome} foi buscar {objeto}"

class Gato(Animal):
    def fazer_som(self):
        return "Miau!"

# Uso
cachorro = Cachorro("Rex")
print(cachorro.fazer_som())  # Au au!
print(cachorro.buscar("bolinha"))  # Rex foi buscar bolinha

gato = Gato("Whiskers")
print(gato.fazer_som())  # Miau!
```

### 1.3 Polimorfismo
Permite que objetos de diferentes classes sejam tratados de forma uniforme.

```python
def fazer_animal_falar(animal):
    """Função que funciona com qualquer Animal"""
    print(animal.fazer_som())

animais = [
    Cachorro("Rex"),
    Gato("Whiskers"),
    Animal("Genérico")
]

for animal in animais:
    fazer_animal_falar(animal)
# Output:
# Au au!
# Miau!
# Som genérico
```

### 1.4 Encapsulamento
Controla o acesso aos atributos e métodos da classe.

```python
class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self._saldo = saldo  # Atributo privado por convenção
        self.__senha = "1234"  # Atributo privado (name mangling)
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
    
    def sacar(self, valor):
        if 0 < valor <= self._saldo:
            self._saldo -= valor
            return True
        return False
    
    @property
    def saldo(self):
        """Getter - acesso de leitura"""
        return self._saldo
    
    @saldo.setter
    def saldo(self, valor):
        """Setter - acesso de escrita"""
        if valor >= 0:
            self._saldo = valor

# Uso
conta = Conta("João", 1000)
print(conta.saldo)  # 1000
conta.depositar(500)
print(conta.saldo)  # 1500
conta.sacar(200)
print(conta.saldo)  # 1300
```

### 1.5 Métodos Especiais
Métodos que começam e terminam com duplo underscore.

```python
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def __str__(self):
        """Representação em string (para print)"""
        return f"Produto: {self.nome} - R${self.preco:.2f}"
    
    def __repr__(self):
        """Representação técnica"""
        return f"Produto('{self.nome}', {self.preco})"
    
    def __eq__(self, outro):
        """Comparação de igualdade"""
        return self.nome == outro.nome and self.preco == outro.preco
    
    def __lt__(self, outro):
        """Comparação menor que"""
        return self.preco < outro.preco
    
    def __add__(self, outro):
        """Adição customizada"""
        return Produto(f"{self.nome} + {outro.nome}", self.preco + outro.preco)
    
    def __len__(self):
        """Comprimento"""
        return len(self.nome)

# Uso
p1 = Produto("Notebook", 2000)
p2 = Produto("Mouse", 50)

print(p1)  # Produto: Notebook - R$2000.00
print(p1 == p2)  # False
print(p2 < p1)  # True
p3 = p1 + p2
print(p3)  # Produto: Notebook + Mouse - R$2050.00
```

### 1.6 Método de Classe e Estático
```python
class Configuracao:
    versao = "1.0"
    contador = 0
    
    def __init__(self):
        Configuracao.contador += 1
    
    @staticmethod
    def informacao_estatica():
        """Não acessa self nem cls"""
        return "Esta é uma informação estática"
    
    @classmethod
    def informacao_classe(cls):
        """Acessa cls (a classe)"""
        return f"Versão: {cls.versao}"
    
    @classmethod
    def criar_com_padrao(cls):
        """Factory method"""
        return cls()

# Uso
print(Configuracao.informacao_estatica())  # Esta é uma informação estática
print(Configuracao.informacao_classe())  # Versão: 1.0

config = Configuracao.criar_com_padrao()
print(Configuracao.contador)  # 1
```

---

## 2. Decoradores

Funções que modificam o comportamento de outras funções ou classes sem alterar seu código.

### 2.1 Decoradores Simples
```python
def meu_decorador(funcao):
    def wrapper(*args, **kwargs):
        print("Antes da execução")
        resultado = funcao(*args, **kwargs)
        print("Depois da execução")
        return resultado
    return wrapper

@meu_decorador
def saudacao(nome):
    print(f"Olá, {nome}!")

saudacao("João")
# Output:
# Antes da execução
# Olá, João!
# Depois da execução
```

### 2.2 Decoradores com Argumentos
```python
def repetir(vezes):
    def decorador(funcao):
        def wrapper(*args, **kwargs):
            for _ in range(vezes):
                resultado = funcao(*args, **kwargs)
            return resultado
        return wrapper
    return decorador

@repetir(3)
def dizerOi():
    print("Oi!")

dizerOi()
# Output:
# Oi!
# Oi!
# Oi!
```

### 2.3 Decoradores Preservando Metadados
```python
import functools

def meu_decorador(funcao):
    @functools.wraps(funcao)  # Preserva metadados da função original
    def wrapper(*args, **kwargs):
        """Wrapper"""
        return funcao(*args, **kwargs)
    return wrapper

@meu_decorador
def funcao_importante():
    """Descrição importante"""
    pass

print(funcao_importante.__name__)  # funcao_importante
print(funcao_importante.__doc__)   # Descrição importante
```

### 2.4 Propriedades (@property)
```python
class Temperatura:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, valor):
        self._celsius = valor

# Uso
temp = Temperatura(0)
print(temp.celsius)      # 0
print(temp.fahrenheit)   # 32.0
temp.celsius = 100
print(temp.fahrenheit)   # 212.0
```

---

## 3. Geradores e Iteradores

### 3.1 Iteradores
Objetos que implementam `__iter__()` e `__next__()`.

```python
class ContadorAte10:
    def __init__(self):
        self.numero = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.numero < 10:
            self.numero += 1
            return self.numero
        else:
            raise StopIteration

# Uso
contador = ContadorAte10()
for numero in contador:
    print(numero)  # 1 a 10
```

### 3.2 Geradores
Funções que retornam valores um de cada vez usando `yield`.

```python
def gerador_numeros(n):
    """Gera números de 1 até n"""
    i = 0
    while i < n:
        yield i
        i += 1

# Uso
for numero in gerador_numeros(5):
    print(numero)  # 0 1 2 3 4

# Criando lista a partir do gerador
numeros = list(gerador_numeros(5))  # [0, 1, 2, 3, 4]
```

### 3.3 Expressões de Gerador
```python
# Sintaxe similar a list comprehension
gerador = (x**2 for x in range(5))
print(next(gerador))  # 0
print(next(gerador))  # 1
print(next(gerador))  # 4

# Convertendo para lista
lista = list(x**2 for x in range(5))  # [0, 1, 4, 9, 16]
```

### 3.4 Geradores com Comunicação Bidirecional
```python
def echo():
    valor = None
    while True:
        valor = yield valor

# Uso
gen = echo()
next(gen)  # Inicia o gerador
print(gen.send(5))  # 5
print(gen.send(10))  # 10
```

---

## 4. Compreensões

### 4.1 List Comprehension
```python
# Forma tradicional
lista = []
for x in range(10):
    if x % 2 == 0:
        lista.append(x**2)

# Compreensão
lista = [x**2 for x in range(10) if x % 2 == 0]
# [0, 4, 16, 36, 64]

# Compreensão aninhada
matriz = [[j for j in range(3)] for i in range(3)]
# [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
```

### 4.2 Dict Comprehension
```python
# Criando dicionário
dicionario = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# De outra estrutura
pares = [('a', 1), ('b', 2), ('c', 3)]
dicionario = {chave: valor for chave, valor in pares}
# {'a': 1, 'b': 2, 'c': 3}
```

### 4.3 Set Comprehension
```python
conjunto = {x**2 for x in range(-3, 4)}
# {0, 1, 4, 9}

# Removendo duplicatas
lista = [1, 1, 2, 2, 3, 3]
conjunto = {x for x in lista}
# {1, 2, 3}
```

---

## 5. Context Managers (with)

### 5.1 Uso Básico
```python
# Operações com arquivo
with open('arquivo.txt', 'r') as arquivo:
    conteudo = arquivo.read()
# Arquivo fecha automaticamente

# Múltiplos arquivos
with open('entrada.txt') as entrada, open('saida.txt', 'w') as saida:
    saida.write(entrada.read())
```

### 5.2 Criando Context Manager
```python
class MeuContextManager:
    def __enter__(self):
        print("Entrando no contexto")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Saindo do contexto")
        return False  # False = propaga exceção

with MeuContextManager() as cm:
    print("Dentro do bloco with")

# Output:
# Entrando no contexto
# Dentro do bloco with
# Saindo do contexto
```

### 5.3 Context Manager com contextlib
```python
from contextlib import contextmanager

@contextmanager
def meu_contexto():
    print("Setup")
    try:
        yield
    finally:
        print("Teardown")

with meu_contexto():
    print("Executando")
```

---

## 6. Tratamento Avançado de Exceções

### 6.1 Exceções Personalizadas
```python
class MinhaExcecao(Exception):
    """Exceção personalizada"""
    pass

class SaldoInsuficiente(Exception):
    def __init__(self, saldo_atual, valor_solicitado):
        self.saldo = saldo_atual
        self.valor = valor_solicitado
        super().__init__(f"Saldo {saldo_atual} < solicitado {valor_solicitado}")

try:
    raise SaldoInsuficiente(100, 200)
except SaldoInsuficiente as e:
    print(f"Erro: {e}")
    print(f"Saldo: {e.saldo}, Solicitado: {e.valor}")
```

### 6.2 Tratamento de Exceções Encadeadas
```python
try:
    resultado = 10 / 0
except ZeroDivisionError as e:
    raise ValueError("Erro ao processar valor") from e

# Output rastreará a exceção original
```

### 6.3 Grupo de Exceções (Python 3.11+)
```python
try:
    # múltiplas operações
    pass
except* ValueError:
    print("Erro de valor")
except* TypeError:
    print("Erro de tipo")
```

---

## 7. Type Hints e Anotações

### 7.1 Type Hints Básicos
```python
def somar(a: int, b: int) -> int:
    return a + b

def processar_dados(dados: list[str]) -> dict[str, int]:
    resultado = {}
    for dado in dados:
        resultado[dado] = len(dado)
    return resultado

# Variáveis com tipo
nome: str = "João"
idade: int = 30
ativo: bool = True
valores: list[int] = [1, 2, 3]
```

### 7.2 Type Hints Complexos
```python
from typing import Optional, Union, Callable, Any

def funcao_complexa(
    valor: int,
    opcional: Optional[str] = None,
    uniao: Union[int, str] = 0,
    callback: Callable[[int], str] = lambda x: str(x),
    generico: Any = None
) -> dict[str, Any]:
    return {"resultado": callback(valor)}
```

---

## 8. Módulos e Pacotes

### 8.1 Importações
```python
# Importação simples
import math
print(math.pi)

# Importação parcial
from math import pi, sqrt
print(pi)

# Importação com alias
import numpy as np
from pandas import DataFrame as DF

# Importação de tudo (não recomendado)
from math import *
```

### 8.2 Criando Módulos
Arquivo `uteis.py`:
```python
def saudacao(nome):
    return f"Olá, {nome}!"

def calcular_media(*valores):
    return sum(valores) / len(valores)
```

Usando:
```python
from uteis import saudacao, calcular_media

print(saudacao("João"))
print(calcular_media(7, 8, 9))
```

### 8.3 Variável `__name__`
```python
def minha_funcao():
    print("Função importante")

if __name__ == "__main__":
    # Executa apenas quando rodado diretamente
    minha_funcao()
```

---

## 9. Paradigmas Funcionais

### 9.1 Map, Filter e Reduce
```python
numeros = [1, 2, 3, 4, 5]

# map - aplica função a todos elementos
dobrados = list(map(lambda x: x * 2, numeros))
# [2, 4, 6, 8, 10]

# filter - filtra elementos
pares = list(filter(lambda x: x % 2 == 0, numeros))
# [2, 4]

# reduce - reduz a um único valor
from functools import reduce
produto = reduce(lambda x, y: x * y, numeros)
# 120
```

### 9.2 Lambda
```python
# Funções anônimas
quadrado = lambda x: x ** 2
print(quadrado(5))  # 25

# Em callbacks
numeros = [3, 1, 4, 1, 5]
print(sorted(numeros, key=lambda x: -x))  # [5, 4, 3, 1, 1]
```

### 9.3 Closures
```python
def criar_multiplicador(n):
    def multiplicar(x):
        return x * n
    return multiplicar

vezes3 = criar_multiplicador(3)
print(vezes3(10))  # 30

vezes5 = criar_multiplicador(5)
print(vezes5(10))  # 50
```

---

## 10. Otimizações

### 10.1 Caching com functools
```python
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))  # Muito mais rápido
```

### 10.2 Slots para Otimização de Memória
```python
class Ponto:
    __slots__ = ['x', 'y']  # Limita atributos
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Economia de memória
p = Ponto(1, 2)
# p.z = 3  # Erro! Só x e y permitidos
```

### 10.3 Operações Vetorizadas
```python
import numpy as np

# Lento
lista = [1, 2, 3, 4, 5]
resultado = [x * 2 for x in lista]

# Rápido
array = np.array([1, 2, 3, 4, 5])
resultado = array * 2
```

---

## 11. Padrões de Design

### 11.1 Singleton
```python
class Singleton:
    _instancia = None
    
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia
```

### 11.2 Factory
```python
class Animal:
    pass

class Cachorro(Animal):
    pass

class Gato(Animal):
    pass

class AnimalFactory:
    @staticmethod
    def criar_animal(tipo):
        if tipo == "cachorro":
            return Cachorro()
        elif tipo == "gato":
            return Gato()
        return None
```

### 11.3 Observer
```python
class Observador:
    def atualizar(self, mensagem):
        pass

class Sujeito:
    def __init__(self):
        self._observadores = []
    
    def attach(self, observador):
        self._observadores.append(observador)
    
    def notificar(self, mensagem):
        for obs in self._observadores:
            obs.atualizar(mensagem)
```

---

## 12. Async/Await

### 12.1 Corrotinas Assíncronas
```python
import asyncio

async def buscar_dados(id):
    print(f"Iniciando busca {id}")
    await asyncio.sleep(2)  # Simula I/O
    print(f"Dados {id} recebidos")
    return f"Dados {id}"

async def main():
    # Execução sequencial
    resultado1 = await buscar_dados(1)
    resultado2 = await buscar_dados(2)
    
    # Execução paralela
    resultados = await asyncio.gather(
        buscar_dados(1),
        buscar_dados(2),
        buscar_dados(3)
    )
    print(resultados)

asyncio.run(main())
```

---

## Conclusão

Os conceitos avançados permitem escrever código mais eficiente, seguro e profissional. A combinação de POO, geradores, decoradores e paradigmas funcionais torna Python uma linguagem extremamente versátil para diversos contextos.
