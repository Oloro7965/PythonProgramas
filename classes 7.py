class tv:
    @staticmethod
    def menu():
        print('O que deseja fazer ?')
        print('1-para ir para o próximo canal')
        print('2-para escolher um canal')
class controle_remoto():
    canal=0
    volume=0
    #def __init__(self,canalnovo):
        #self.canalnovo=canalnovo
    @staticmethod
    def escolha():
        escolha= int(input('Sua escolha '))
        while escolha>2 or escolha<1:
            print('escolha inválida')
            escolha=int(input('Sua escolha '))
        if escolha==1:
            controle_remoto.proximo_canal()
        if escolha==2:
            canaln=int(input('digite o canal desejado '))
            controle_remoto.set_canal(canaln)
    @classmethod
    def proximo_canal(cls):
        cls.canal += 1
        controle_remoto.canal_atual()
    @classmethod
    def set_canal(cls,canalnovo):
        cls.canal=canalnovo
    @classmethod
    def canal_atual(cls):
        print(f'Você está no canal {cls.canal}')
tv.menu()
controle_remoto.escolha()

