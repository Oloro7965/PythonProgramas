class civil:
    contador=0
    #@classmethod
    #ef menu(cls):
        #print(f'Seja bem vindo a calculadora de IMC')
        #altura=float(input('digite a sua altura '))
        #peso=float(input('digite o seu peso '))
        #p=civil(altura,peso)
        #p.calcular()
        #cls.contador += 1
    @staticmethod
    def menu():
        print(f'Seja bem vindo a calculadora de IMC')
        altura=float(input('digite a sua altura '))
        peso=float(input('digite o seu peso '))
        p=civil(altura,peso)
        p.calcular()
        civil.contador+=1
    def __init__(self,altura, peso):
        self.altura=altura
        self.peso=peso
        civil.contador+=1
        self.imc=(self.peso)/(self.altura**2)
    def calcular(self):
        print(f'IMC de {self.imc}')
    def exibir_cont(self):
        print(f'tem {civil.contador} pessoas ')
#print(civil.contador)
civil.menu()
#altura=float(input('digite a sua altura '))
#peso=float(input('digite o seu peso '))
#p1=civil(altura,peso)
#p1.calcular()


