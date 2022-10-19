"""
Decorators
Funções de maior grandeza- Higher order functions
Quando uma linguagem de programação permite utilizarmos funções de maior grandeza, significa que podemos
ter funções que
retornam outras funções como resultado ou que podemos criar funções que usam outras funções como argumento,
ou até criar
variáveis do tipo de funções nos nossos programas
"""
from random import choice
def somar(a,b):
    return a+b

def diminui(a,b):
    return a-b

def multiplicar(a,b):
    return a*b


def dividir(a,b):
    return a/b

def calcular(a,b,funcao):
    return funcao(a,b)
def cumprimentar(pessoa):
    def humor():
        return choice(('sai daqui','sandro é bi ','sandro n é bi '))
    return humor() + pessoa
print(calcular(2,3,somar))
print(calcular(2,3,diminui))
print(calcular(2,3,multiplicar))
print(calcular(2,3,dividir))
print(cumprimentar('pedro'))