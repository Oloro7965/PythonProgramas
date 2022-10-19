"""
Metadatas-são dados intrisecos em arquivos
wraps-são funções que envolvem elementos com diversas finalidades

"""

#preservando metadata com wraps
from functools import wraps
def ver_log(funcao):
    @wraps(funcao)
    def logar(*args,**kwargs):
       """função logar dentro de outra"""
       print(f'você está chamando a função {funcao.__name__}')
       print(f'aqui está a documentação:{funcao.__doc__}')
       return funcao(*args,**kwargs)
    return logar

@ver_log
def soma(a,b):
    """Soma dois números"""
    return a+b
print(soma(120,344))
print(soma.__name__)
print(soma.__doc__)


