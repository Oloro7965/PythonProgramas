import player,time
class jogoDaVelha:
    def __init__(self,x_player,o_player):
        #self.__lista=[['_','_','_'],['_','_','_'],['_','_','_']]
        self.__lista = ['_' for _ in range(9)]
        self.__movimentos_disponiveis = [i+1 for i,spot in enumerate(self.lista) if spot == '_']
        self.__x_player = x_player
        self.__o_player = o_player
        self.__current_winner = None
        self.__game_over = False
        self.__game_draw = False
        self.jogar()
    @property
    def lista(self):
        return self.__lista
    def jogar(self):
        jogoDaVelha.mostrar_tabuleiro_nums()
        self.mostrarTabuleiro()
        while not self.__game_over:
            move_x = self.__x_player.get_move()
            while move_x not in self.__movimentos_disponiveis:
                print('movimento inválido')
                move_x = self.__x_player.get_move()
            if move_x in self.__movimentos_disponiveis:
                self.lista[move_x-1] = 'X'
                self.__movimentos_disponiveis.remove(move_x)
                if self.verificaGanhador():
                    self.__current_winner = 'X'
                    self.__game_over = True
                    self.mostrarTabuleiro()
                    break
            self.mostrarTabuleiro()
            print(self.__movimentos_disponiveis)
            if self.game_draw():
                self.__game_draw=True
                self.__game_over=True
                break
            # move_o = self.__o_player.get_move()
            time.sleep(3)
            move_o=self.__o_player.get_move(self.__movimentos_disponiveis)
            print(move_o)
            while (move_o) not in self.__movimentos_disponiveis:
                print('movimento inválido')
                move_o = self.__o_player.get_move(self.__movimentos_disponiveis)
            if (move_o) in self.__movimentos_disponiveis:
                self.lista[move_o-1] = 'O'
                self.__movimentos_disponiveis.remove(move_o)
                if self.verificaGanhador():
                    self.__current_winner = 'O'
                    self.__game_over = True
                    self.mostrarTabuleiro()
            self.mostrarTabuleiro()
            if self.game_draw():
                self.__game_over=True
                self.__game_draw=True
            print(self.__movimentos_disponiveis)
        if self.__game_draw:
            print('its a draw!')
        else:
            print('O jogador '+self.__current_winner+' ganhou!')
    @staticmethod
    def mostrar_tabuleiro_nums():
        number_board = [[str(i+1) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row)+' |')
    def mostrarTabuleiro(self):
        for row in [self.__lista[i*3:(i+1)*3] for i in range(3)]:
            for number in row:
                print(f'{number} ',end='')
            print()
    def verificaGanhador(self):
        #linha
        for row in [self.__lista[i * 3:(i + 1) * 3] for i in range(3)]:
            if row[0] == row[1] == row[2] and row[0] != '_':
                return True
        #coluna
        for column in [[self.lista[i],self.lista[i+3],self.lista[i+6]] for i in range(3)]:
            if column[0] == column[1] == column[2] and column[0] != '_':
                return True
        #Diagonais
        if self.lista[0]==self.lista[4]==self.lista[8] and self.lista[0] != '_':
            return True
        if self.lista[2]==self.lista[4]==self.lista[6] and self.lista[2] != '_':
            return True
        return False
    def game_draw(self):
        if len(self.__movimentos_disponiveis) == 0:
            return True
        return False
if __name__=='__main__':
    x_player = player.Human_player('X')
    o_player = player.Random_computer('O')
    game = jogoDaVelha(x_player,o_player)

