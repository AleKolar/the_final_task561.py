from IPython.display import clear_output
import random


def create_board(board):  # создаем игровое поле
    clear_output()
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('_' * 9)
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('_' * 9)
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])


def player_x_or_o():  # Выбор символа(Х или О)
    marker = ''
    while marker != "X" or marker != "O":  # валидация пусть будет здесь, в ф-ии выбора ( или надо одна ф-ия, – одно действие !? )
        marker = str(input("player1 введите символ, чем будете играть: x или o?: ").upper())
        if marker == 'X':
            return ('X', 'O')  # здесь кортеж, чтоб 2-му игроку присвоить оставшийся символ при распаковке
        else:
            if marker == 'O':  # пока не было if цикл while не отрабатывал, пробрвал конструкцию try/except, я так и не понял в чем дело
                return ('O', 'X')


def boardplace_of_marker(board, marker, position):  # ф-ия помещает  символ в выбранную клетку
    board[position] = marker


def win_combo(board, mark):  # выигрышные комбинации
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or  # от цикла отказался
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[1] == mark and board[4] == mark and board[7] == mark) or
            (board[2] == mark and board[5] == mark and board[8] == mark) or
            (board[3] == mark and board[6] == mark and board[9] == mark) or
            (board[1] == mark and board[5] == mark and board[9] == mark) or
            (board[3] == mark and board[5] == mark and board[7] == mark))


def who_first_step():  # определяем:чей первый ход
    step = random.randint(1, 2)
    if step == 1:
        return "player1"
    else:
        return "player2"


def check_ceil_empty(board, position):  # ф-ия проверяет занятость позиции
    return board[position] == ' '


def check_full_fill(board):  # ф-ия проверяет полностью ли занято игровое поле
    for i in range(1, 10):
        if check_ceil_empty(board, i):
            return False
    return True


def player_choice(board):  # ф-ия осуществляет выбор клетки игроком и затем(в реализации) ф-ия boardplace_of_marker помещает символ в клетку
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not check_ceil_empty(board, position):
        position = int(input("Укажите поле от 1 до 9:"))
    return position


def replay():  # ф-ия для продолжения/прекращения игры
    choice = input("Хотите играть дальше? Введите Y или N").lower()
    return choice == 'y'


# Р Е А Л И З А Ц И Я
print("Начнем!")

game_on = True

while True:

    board = [' '] * 10
    player1, player2 = player_x_or_o()

    turn = who_first_step()  # в turn сохраним игрока, кто ходит первым
    print("Первым ходит", turn)

    game_on = True
    while game_on:
        if turn == "player1":
            create_board(board)  # вывели поле
            position = player_choice(board)  # player1 выбирает клетку
            boardplace_of_marker(board, player1, position)  # помещаем символ в выбранную клетку

            if win_combo(board, player1):  # проверим выигрышные комбинации
                create_board(board)  # увидим это на игровом поле
                print("player1_выиграл!")
                create_board(board)
                game_on = False  # всЁ., игроки прекращают делать ходы по очереди
            else:
                if check_full_fill(board):
                    create_board(board)
                    print("Ничья!")
                    create_board(board)
                    game_on = False  # всё., игроки прекращают делать ходы по очереди
                else:
                    turn = "player2"

        else:
            create_board(board)
            position = player_choice(board)
            boardplace_of_marker(board, player2, position)

            if win_combo(board, player2):
                create_board(board)
                print("player2_выиграл!")
                create_board(board)
                game_on = False
            else:
                if check_full_fill(board):
                    create_board(board)
                    print("Ничья!")
                    create_board(board)
                    game_on = False
                else:
                    turn = "player1"

    if not replay():
        break
