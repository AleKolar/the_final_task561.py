import random


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


class Player(Board):

    def __init__(self, position):
        super().__init__()
        self.position = position
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

    def vacant_or_occuped(self):
        if not self.used:
            while self.position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] and self.used is False:
                Board.position = input("Укажите поле от 1 до 9:")
            self.used = True
            self.board[self.position] = self.marker
            print(Board.create_board(self))
            return self.position


class Game(Player):

    def __init__(self):
        super().__init__(self)
        self.player = ['X', 'O']
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





b = Player(5)
b.first_step()



b.vacant_or_occuped()
b = Player(5)
b.vacant_or_occuped()