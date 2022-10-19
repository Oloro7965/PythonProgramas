class jogoDaVelha:
    def __init__(self):
        #self.__lista=[['_','_','_'],['_','_','_'],['_','_','_']]
        self.__lista = ['_' for _ in range(9)]
        self.__movimentos_disponiveis=[i for i,spot in enumerate(self.lista) if spot == '_']
    @property
    def lista(self):
        return self.__lista
    def jogar(self):
        self.mostrarTabuleiro()
        self.jogador1()
    def jogador1(self):
        print('Jogador 1')
        position = int(input('digite a posição '))
        if self.lista[position-1] == '_':
            self.lista[position-1] = 'X'
            if self.verificaGanhador():
                print('jogador 1 ganhou')
                self.mostrarTabuleiro()
            else:
                self.mostrarTabuleiro()
                self.jogador2()
        else:
            print('jogada inválida, tente novamente')
            self.jogador1()
    def jogador2(self):
        print('Jogador 2')
        position = int(input('digite a posição '))
        if self.__lista[position-1] == '_':
            self.__lista[position-1] = '0'
            if self.verificaGanhador():
                print('jogador 2 ganhou')
                self.mostrarTabuleiro()
            else:
                self.mostrarTabuleiro()
                self.jogador1()
        else:
            print('jogada inválida,tente novamente')
            self.jogador2()
    def mostrarTabuleiro(self):
        # for cont in range(0,3):
        # for linha in self.lista:
        #     for col in linha:
        #         print(f'{col} ',end='')
        #     print()
        for row in [self.__lista[i*3:(i+1)*3] for i in range(3)]:
            for number in row:
                print(f'{number} ',end='')
            print()
        # print([self.__lista[i*3:(i+1)*3] for i in range(3)])
    def verificaGanhador(self):
        # #linha
        # for i in range(3):
        #     if self.lista[i][0]==self.lista[i][1]==self.lista[i][2] and self.lista[i][0]!='_':
        #         return True
        # #coluna
        # for c in range(3):
        #     if self.lista[0][c]==self.lista[1][c]==self.lista[2][c] and self.lista[0][c]!='_':
        #         return True
        # if self.lista[0][0]==self.lista[1][1]==self.lista[2][2] and self.lista[0][0]!='_':
        #     return True
        # if self.lista[2][0]==self.lista[1][1]==self.lista[0][2] and self.lista[2][0]!='_':
        #     return True
        #linha
        for row in [self.__lista[i * 3:(i + 1) * 3] for i in range(3)]:
            if row[0] == row[1] == row[2] and row[0] != '_':
                return True
        #coluna
        for column in [[self.lista[i],self.lista[i+3],self.lista[i+6]] for i in range(3)]:
            if column[0] == column[1] == column[2] and column[0] != '_':
                return True
        if self.lista[0]==self.lista[4]==self.lista[8] and self.lista[0] !='_':
            return True
        if self.lista[2]==self.lista[4]==self.lista[6] and self.lista[2] != '_':
            return True
        return False
jogo=jogoDaVelha()
jogo.jogar()

