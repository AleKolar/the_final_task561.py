import random


class Board:

    def __init__(self):
        self.position = []
        for position in range(1, 10):
            self.position.append(position)
        self.marker = ''
        self.board = [int(i) for i in range(0, 10)]
        self.used = False

    def create_board(self):  # создаем игровое поле
        print(self.board[1], ' | ', self.board[2], ' | ', self.board[3])
        print('_' * 14)
        print(self.board[4], ' | ', self.board[5], ' | ', self.board[6])
        print('_' * 14)
        print(self.board[7], ' | ', self.board[8], ' | ', self.board[9])

    def check_ceil_empty(self):  # ф-ия проверяет занятость позиции
        if self.board[self.position] == '':
            return False
        return True

    def check_full_fill(self):  # ф-ия проверяет полностью ли занято игровое поле
        for i in range(1, 10):
            if self.check_ceil_empty:
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
            return 'X', 'O'
        else:
            self.marker = 'O'
            print(f'Первым ходит player{self.marker}')
            return 'O', 'X'

    def choice_player(self):
        position = 0
        if not self.used:
            while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] and self.board[self.position] != '':
                position = int(input("Укажите поле от 1 до 9:"))
                self.used = True
                self.position = position
                return self.set_marker()
            else:
                self.check_full_fill()

    def set_marker(self):
        self.board[self.position] = self.marker

    def win_combo(self):
        if ((self.board[1] == self.player and self.board[2] == self.player and self.board[3] == self.player) or
                (self.board[4] == self.player and self.board[5] == self.player and self.board[6] == self.player) or
                (self.board[7] == self.player and self.board[8] == self.player and self.board[9] == self.player) or
                (self.board[1] == self.player and self.board[4] == self.player and self.board[7] == self.player) or
                (self.board[2] == self.player and self.board[5] == self.player and self.board[8] == self.player) or
                (self.board[3] == self.player and self.board[6] == self.player and self.board[9] == self.player) or
                (self.board[1] == self.player and self.board[5] == self.player and self.board[9] == self.player) or
                (self.board[3] == self.player and self.board[5] == self.player and self.board[7] == self.player)):
            self.win = True
            print(f'Победил player{self.player}')
        else:
            print(f'Ничья')

    def game(self):
        while self.check_full_fill() == False and self.win == False:
            print(a.choice_player(), a.create_board())
            return self.choice_player()


a = Player()
a.first_step()
a.game()
