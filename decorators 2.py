"""
Decorators
-São funções
-Envolvem outras funções e aprimoram seus comportamentos
-também são exemplos de funções de maior grandeza
-tem uma sintaxe própria,usando @
"""
#decorators como funções(sintaxe não recomendada)
def seja_educado(funcao):
    def sendo():
        print('foi um prazer conhecer você')
        funcao()
        print('tenha um ótimo dia')
    return sendo
def saudacao():
    print('seja bem-vindo a geek university')

teste=seja_educado(saudacao)
teste()
print()
#2-sintaxe correta
def seja_educadomesmo(funcao):
    def sendo_mesmo():
        print('foi um prazer te conhecer')
        funcao()
        print('tenha um excelente dia')
    return sendo_mesmo
@seja_educadomesmo
def apresentando():
    print('Meu nome é Pedro')
apresentando()
