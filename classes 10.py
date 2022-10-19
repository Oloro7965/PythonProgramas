class pessoa:
    def __init__(self,nome='',endereco='',telefone=''):
        self.nome=str(input('digite o nome '))
        self.endereco=str(input('digite o endereço '))
        self.telefone=str(input('digite o telefone '))
    def imprimir(self):
        print(f'nome-{self.nome}\nendereço-{self.endereco}\ntelefone-{self.telefone}')
p1=pessoa('','','')
p1.imprimir()

