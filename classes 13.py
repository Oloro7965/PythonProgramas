class retangulo:
    def __init__(self,comprimento,largura):
        self.comprimento=comprimento
        self.largura=largura
    def valor_lados(self):
        print(f'comprimento-{self.comprimento}\nlargura-{self.largura}')
    def set_lados(self):
        print('Digite as medidas novas')
        comprimento_novo=int(input('Comprimento\n'))
        largura_nova=int(input('Largura\n'))
        self.comprimento=comprimento_novo
        self.largura=largura_nova
        ret_novo=retangulo(self.comprimento,self.largura)
        print('valores alterados com sucesso')
        ret_novo.valor_lados()
    def calcular_area(self):
        return self.comprimento*self.largura
    def perimetro(self):
        return (self.comprimento*2)+(self.largura*2)
r1=retangulo(10,4)
r1.valor_lados()
print(r1.calcular_area())
r1.set_lados()
print(r1.calcular_area())
comprimento=int(input('digite o comprimento do local '))
largura=int(input('digite a largura do local '))
r2=retangulo(comprimento,largura)

