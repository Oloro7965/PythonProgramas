class retangulo:
    def __init__(self,comprimento,largura):
        self.__comprimento=comprimento
        self.__largura=largura
        self.__area=self.__comprimento*self.__largura
        self.__perimetro=(self.__comprimento+self.__largura)*2
    def __repr__(self):
        return f'comprimento-{self.__comprimento}\nlargura-{self.__largura}\narea-{self.__area}\nperimetro-{self.__perimetro}'
    #def imprimir(self):
        #for k,v in ret.__dict__.items():
            #print(f'{k}-{v}')
    def calcular_area(self):
        return f'a área do retângulo é {self.__area}'
    def calcular_perimetro(self):
        return f'o perímetro do retângulo é {self.__perimetro}'
a=float(input('digite o comprimento '))
b=float(input('digite a largura '))
ret=retangulo(a,b)
#print(ret.calcular_area())
#print(ret.calcular_perimetro())
#ret.imprimir()
print(ret)




