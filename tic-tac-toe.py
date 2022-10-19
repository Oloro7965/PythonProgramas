
class game:
    def __init__(self):
        self.board = ['_' for _ in range(9)]
        self.current_winner = None
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print(row)
    def board_nums(self):
        number_board = [[str(i) for i in range((j*3)+1,((j+1)*3)+1)] for j in range(3)]
        for row in number_board:
            for number in row:
                print(number,end='')
            print()
jogo = game()
jogo.print_board()
jogo.board_nums()