"""
#com o now,conseguimos especificar um fuso-horário
agora=datetime.datetime.now()
print(agora)
print(type(agora))
print(repr(agora))
#
hoje=datetime.datetime.today()
print(hoje)
print(type(hoje))
print(repr(hoje))

#manutenção de 1 em 1 dia, a meia noite
manutencao=datetime.datetime.combine((datetime.datetime.now()+datetime.timedelta(days=1)),datetime.time())
print(manutencao)
print(type(manutencao))
print(repr(manutencao))

#encontrar o dia da semana
#os dias da semana do método weekday começam em 0, sendo esta a segunda-feira
#0-segunda-feira
#1-terça-feira
#2-quarta-feira
#3-quinta-feira
#4-sexta-feira
#5-sábado
#6-domingo
manutencao=datetime.datetime.combine((datetime.datetime.now()+datetime.timedelta(days=1)),datetime.time())
print(manutencao)
print(manutencao.weekday())

aniversario=input('qual é o seu aniversário ')
aniversario=aniversario.split('/')
aniversario=datetime.datetime(year=int(aniversario[2]),month=int(aniversario[1]),day=int(aniversario[0]))
if aniversario.weekday()==0:
    print('você nasceu numa segunda-feira')
elif aniversario.weekday()==1:
    print('você nasceu numa terça-feira')
elif aniversario.weekday()==2:
    print('você nasceu numa quarta-feira')
elif aniversario.weekday()==3:
    print('você nasceu numa quinta-feira')
elif aniversario.weekday()==4:
    print('você nasceu numa sexta-feira')
elif aniversario.weekday()==5:
    print('você nasceu num sábado')
elif aniversario.weekday()==6:
    print('você nasceu num domingo')


#formatando datas com strftime
#dd/mm/aa
def formata_data(data):
    if data.month==1:
        print(f'{data.day} de janeiro de {data.year}')
    elif data.month==2:
        print(f'{data.day} de fevereiro de {data.year}')
    elif data.month==3:
        print(f'{data.day} de março de {data.year}')
    elif data.month==4:
        print(f'{data.day} de abril de {data.year}')
    elif data.month==5:
        print(f'{data.day} de maio de {data.year}')
    elif data.month==6:
        print(f'{data.day} de junho de {data.year}')
    elif data.month==7:
        print(f'{data.day} de julho de {data.year}')
    elif data.month==8:
        print(f'{data.day} de agosto de {data.year}')
    elif data.month==9:
        print(f'{data.day} de setembro de {data.year}')
    elif data.month==10:
        print(f'{data.day} de outubro de {data.year}')
    elif data.month==11:
        print(f'{data.day} de novembro de {data.year}')
    elif data.month==12:
        print(f'{data.day} de dezembro de {data.year}')
hoje=datetime.datetime.today()
#print(hoje)
formata_data(hoje)
hoje_formatado=hoje.strftime('%d/%m/%Y')
print(hoje_formatado)

#formato mais compacto
def formata_data(data):
    return f"{data.day} de {TextBlob(data.strftime('%B')).translate(to='pt-br')}"
evento=datetime.datetime.now()
print(formata_data(evento))

#detecção de linguagem
user=input('digite uma frase ')
print(TextBlob(user).detect_language())



def formata_data(data):
    return f"{data.day} de {TextBlob(data.strftime('%B')).translate(to='pt')} de {data.year}"
data=input('digite uma data ')
data=data.split('/')
data=datetime.datetime(year=int(data[2]),month=int(data[1]),day=int(data[0]))
print(formata_data(data))
"""
import datetime
from textblob import TextBlob
data=input('digite uma data ')
data=datetime.datetime.strptime(data,'%d/%m/%Y')
print(f"{data.day} de {TextBlob(data.strftime('%B')).translate(to='pt')} do ano de {data.year}")
