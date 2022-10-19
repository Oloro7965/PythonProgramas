class comodo:
    def __init__(self,comprimento,largura):
        self.comprimento=comprimento
        self.largura=largura
        self.perimetro=(self.comprimento*2)+(self.largura*2)
        self.area=self.comprimento * self.largura
    def perimetro(self):
        return self.perimetro()
    def area(self):
        return self.area()
    def quant_lampadas(self):
        if self.area<=6:
            print('Deverá ser colocado 1 ponto de iluminação de 100VA')
        else:
            cont100=1
            cont60=0
            area2=self.area-6
            quant=area2/4
            print(f'Deverão ser colocados {cont100} pontos de 100VA e {int(quant)} pontos de 60VA')
    def quant_tomadas(self):
        print('Escolha a opção de tipo de cômodo')
        print('1-copas,cozinhas,áreas de serviço')
        print('2-outros cômodos')
        escolha=int(input('Sua escolha '))
        if escolha==1:
            quant_tomadas=self.perimetro/3.2
            print(f'Deverão ser colocados {round(quant_tomadas)} pontos de tomada, sendo 3 deles de 100VA e o resto de 100VA')
        if escolha==2:
            quant_tomadas=self.perimetro/5
            print(f'Deverão ser colocados {round(quant_tomadas)} pontos de tomada, sendo 3 deles de 100VA e o resto de 100VA')
c1=comodo(11,3)
print(c1.area)
print(c1.perimetro)
c1.quant_lampadas()
c1.quant_tomadas()


