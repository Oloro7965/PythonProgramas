class tv:
    def __init__(self,canal,volume):
        self.canal = canal
        self.volume = volume
class controle_remoto(tv):
    def __init__(self,canal,volume):
        super().__init__(canal,volume)
        #self.canal=canal
        #self.volume=volume
    def controle_de_canal(self):
        print('1-para aumentar ')
        print('2 para diminuir ')
        print('3 para escolher o canal ')
        user=int(input('digite a opção '))
        if user==1:
            self.canal+=1
            print(f'canal alterado com sucesso para {self.canal}')
        if user==2:
            self.canal-=1
            print(f'canal alterado com sucesso para {self.canal}')
        if user==3:
            escolha=int(input('digite o canal para o qual deseja mudar '))
            controle_remoto.canaln(self,escolha)
    def canal(self):
        return self.canal
    def canaln(self,canal_novo):
        self.canal = canal_novo
        print(f'canal alterado com sucesso para {self.canal}')
    def volume(self):
        return self.volume
    def aumentar_volume(self):
        self.volume+=1
    def diminuir_volume(self):
        self.volume-=1
p1 = controle_remoto(1,0)
p1.controle_de_canal()
print(p1.volume)
print(p1.canal)




