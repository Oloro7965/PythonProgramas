class elevador:
    def __init__(self,andar_atual,total,capacidade,quant_pessoas):
        self.andar_atual=andar_atual
        self.total=total
        self.capacidade=capacidade
        self.quant_pessoas=quant_pessoas
    def inicializar(self,quant_pessoas=0,andar_atual=0):
        self.quant_pessoas=0
        self.andar_atual=0
    def entra(self):
        if self.quant_pessoas<self.capacidade:
            self.quant_pessoas+=1
            print(f'1 pessoa foi adicionada.\n{self.quant_pessoas} pessoas estão no elevador')
    def sai(self):
        if self.quant_pessoas>0:
            self.quant_pessoas-=1
            print(f'1 pessoa foi removida.\n{self.quant_pessoas} pessoas estão no elevador')
    def sobe(self):
        if self.andar_atual<self.total:
            self.andar_atual+=1
            print(f'atualmente estamos no {self.andar_atual} andar')
    def desce(self):
        if self.andar_atual>0:
            self.andar_atual-=1
            print(f'atualmente estamos no {self.andar_atual} andar')
    @property
    def andar(self):
        return self.andar_atual
    @andar.setter
    def andar(self,andar_novo):
        self.andar_atual=andar_novo
    @property
    def quantidade(self):
        return self.quant_pessoas
    @quantidade.setter
    def quantidade(self,quant_nova):
        self.quant_pessoas=quant_nova
    @property
    def totaldeandares(self):
        return self.total
e1=elevador(0,15,10,2)
e1.inicializar()
e1.entra()
e1.entra()
e1.sobe()
e1.sobe()



