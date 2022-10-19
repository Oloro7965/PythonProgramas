#dicionario={"Nome":input("digite o nome"),"Idade":int(input("digite a idade")),"Profissão":input("digite a profissão")}
#print(dicionario)
def criar_conta(nome,idade,profissao):
    conta={"Nome":nome,"Idade":idade,"Profissão":profissao}
    print("Conta criada com sucesso")
    return conta
def get_dados(tipo_de_dados,conta):
    for k,v in conta.items():
        if k==tipo_de_dados:
            print(f'{v}')
Nome=input("digite o nome ")
Idade=int(input("digite a idade "))
Profissao=input("digite a profissão ")
Conta=criar_conta(Nome,Idade,Profissao)
print(Conta)
get_dados("Profissão",Conta)


