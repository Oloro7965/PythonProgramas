"""
Lendo arquivos CSV
duas formas do python pra ler arquivos CSV
-reader(): permite que iteremos sobre as linhas do arquivo como listas
-ordered dict
-forma errada
with open("lutadores (1).csv",encoding='utf-8') as arquivo:
    dados = arquivo.readlines()
    print(type(dados))
    print(dados)
    print(dados[1:])
    for dado in dados:
        print(dado)
    #print(dados.split(',')[:])

forma certa
#Reader(retorna um iterator):
from csv import reader
with open("lutadores (1).csv",encoding='utf-8') as arquivo:
    leitor_csv=reader(arquivo)
    print(type(leitor_csv))
    next(leitor_csv)
    for linha in leitor_csv:
            print(f'{linha[0]} nasceu no {linha[1]} e tem {linha[2]} cm de altura')

#Ordered dict

"""
from csv import DictReader
with open('lutadores (1).csv',encoding='utf-8') as arquivo:
    leitor_csv=DictReader(arquivo)
    for linha in leitor_csv:
        print(f'{linha["Nome"]} nasceu no {linha["País"]} e tem {linha["Altura (em cm)"]}')

