import random

MARK = ''
class Board:

    def __init__(self):
        self.marker = ''
        self.board = [' '] * 10
        self.used = False

    def create_board(self):  # создаем игровое поле
        print(self.board[1] + ' | ' + self.board[2] + ' | ' + self.board[3])
        print('_' * 9)
        print(self.board[4] + ' | ' + self.board[5] + ' | ' + self.board[6])
        print('_' * 9)
        print(self.board[7] + ' | ' + self.board[8] + ' | ' + self.board[9])

    def __getitem__(self, item):
        return self.board[item]

    def check_ceil_empty(self):  # ф-ия проверяет занятость позиции
        return self.board[self.position] == ' '

    def check_full_fill(self):  # ф-ия проверяет полностью ли занято игровое поле
        for i in range(1, 10):
            if self.check_ceil_empty():
                return False
        return True


class Player(Board):

    def __init__(self):
        super().__init__()
        self.position = 0
        self.player = random.randint(1, 2)
        self.win = False

    def first_step(self):
        if self.player == 1:
            self.marker = 'X'
            print(f'Первым ходит player{self.marker}')
            return self.marker
        else:
            self.marker = 'O'
            print(f'Первым ходит player{self.marker}')
            return self.marker

    def choice_player(self):
        position = 0
        if not self.used:
            while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] and self.board[self.position] != MARK:
                position = int(input("Укажите поле от 1 до 9:"))
                self.used = True
                self.position = position
                return self.setMarker()
            else:
                self.check_full_fill()


    def setMarker(self):
        self.board[self.position] = self.marker


class Game(Player):

    def __init__(self):
        super().__init__()
        self.board = Board()
        self.game_on = True

    def __getitem__(self, item: object):
        return self.board[item]

    def win_combo(self):
        if ((self.board[1] == self.player and self.board[2] == self.player and self.board[3] == self.player) or
                (self.board[4] == self.player and self.board[5] == self.player and self.board[6] == self.player) or
                (self.board[7] == self.player and self.board[8] == self.player and self.board[9] == self.player) or
                (self.board[1] == self.player and self.board[4] == self.player and self.board[7] == self.player) or
                (self.board[2] == self.player and self.board[5] == self.player and self.board[8] == self.player) or
                (self.board[3] == self.player and self.board[6] == self.player and self.board[9] == self.player) or
                (self.board[1] == self.player and self.board[5] == self.player and self.board[9] == self.player) or
                (self.board[3] == self.player and self.board[5] == self.player and self.board[7] == self.player)):
            self.game_on = False
            print(f'Победил player{self.player}')





b = Player()
b.first_step()
b.choice_player()
b.create_board()


