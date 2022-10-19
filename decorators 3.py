"""
Decorators
-São funções
-Envolvem outras funções e aprimoram seus comportamentos
-também são exemplos de funções de maior grandeza
-tem uma sintaxe própria,usando @

Decoradores- assinatura

def civil(funcao):
    def civil2():
        print('eu sou civil')
    return civil2
@civil
def sandro():
    print('sandro é bi ')
sandro()

def gritar(funcao):
    def aumentar(nome):
        return funcao(nome)
    return aumentar
@gritar
def saudacao(nome):
    print(f'Olá,meu nome é {nome}')
@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, gostaria de pedir {principal} com {acompanhamento} de acompanhamento'

saudacao('pedro')
print(ordenar('picanha','batata'))

A assinatura de uma função são o seu nome, retorno e parâmetros de entrada

def gritar(funcao):
    def aumentar(*args,**kwargs):
        return funcao(*args,**kwargs)
    return aumentar
@gritar
def saudacao(nome):
    print(f'Olá,meu nome é {nome}')
@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, gostaria de pedir {principal} com {acompanhamento} de acompanhamento'

saudacao('pedro')
print(ordenar('picanha','batata'))
print(ordenar(principal='picanha',acompanhamento='sandro'))
"""
#refatorando com a decorator pattern
def verifica_primeiro_valor(valor):
    def interna(funcao):
        def outra(*args,**kwargs):
            if args[0]!=valor:
                return f'Valor incorreto.Primeiro argumento precisa ser {valor}'
            return funcao(*args,**kwargs)
        return outra
    return interna

@verifica_primeiro_valor('pizza')
def comida_favorita(*args):
     return args

@verifica_primeiro_valor(10)
def soma_dez(n1,n2):
    return n1+n2

print(soma_dez(10,12))
print(comida_favorita('sandro','sandro'))




