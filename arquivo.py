"""
Escrevendo em arquivos csv
#writer
from csv import writer
with open('civis.csv','w') as arquivo:
    escritor_csv=writer(arquivo)
    filme=None
    escritor_csv.writerow(['Título', 'Gênero' ,'Duração'])
    while filme != 'sair':
        filme = input('digite o nome do filme ')
        if filme != 'sair':
            genero=input('digite o gênero ')
            duracao=input('digite a duração ')
            escritor_csv.writerow([filme, genero, duracao])

"""
#dict writer
from csv import DictWriter
with open('civis3.csv','w') as arquivo:
    cabecalho=['Título', 'Gênero', 'Duração']
    escritor_csv=DictWriter(arquivo,fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme=None
    while filme != 'sair':
        filme = input('digite o nome do filme ')
        if filme != 'sair':
            genero=input('digite o gênero ')
            duracao=input('digite a duração ')
            escritor_csv.writerow({'Título':filme,'Gênero':genero,'Duração':duracao})




