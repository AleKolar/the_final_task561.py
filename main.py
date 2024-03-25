from IPython.display import clear_output
import random

def create_board(board):
    clear_output()
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    #print('_' * 9)
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    #print('_' * 9)
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])


test_board = ['#'] + [' '] * 9
create_board(test_board)
'''def numeric_board(test_board):
    cnt = 0
    for i in range(1, len(test_board)):
        cnt += 1
        test_board[i] += str(cnt)
    print(test_board)
numeric_board(test_board)''' # Цифры в клетках отвлекают, не оч.хорошее решение и из-за способа отображения клетки плывут



def player_x_or_y():
    marker = ''
    while marker != 'X' or marker != 'O': # валидация пусть будет здесь, в ф-ии выбора
        try:
            marker = input("player1 введите чем будете играть x или o: ").upper()
            if marker == 'X':
                return ('X', 'O') # здесь кортеж, чтоб 2-му игроку автоматически присвоить оставшийся символ
            elif marker == 'O':
                return ('O', 'X')
            else:
                raise TypeError
        except:
            print("Введите X или O, O и X - англ. буквы 'O' и 'X")


#player1, player2 = player_x_or_y()


def boardplace_of_marker(board, marker, position):
    board[position] = marker

boardplace_of_marker(test_board, 'X', 7)
create_board(test_board)


def win_combo(board, mark): # от цикла отказался
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[1] == mark and board[4] == mark and board[7] == mark) or
            (board[2] == mark and board[5] == mark and board[8] == mark) or
            (board[3] == mark and board[6] == mark and board[9] == mark) or
            (board[1] == mark and board[5] == mark and board[9] == mark) or
            (board[3] == mark and board[5] == mark and board[7] == mark))

def who_first_step():
    step = random.randint(1, 2)
    if step == 1:
        return "player1 ходит первым"
    else:
        return "player2 ходит первым"

def check_ceil_empty(board, position):
    return board[position] == ' '

def check_full_fill(board):
    for i in range(1, 10):
        if check_ceil_empty(board, i):
            return False
    return True

def player_choice(board):
    position = 0 # Это я "скопипастил", но это лучше, чем было
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not check_ceil_empty(board, position):
        position = int(input("Укажите поле от 1 до 9:"))
    return position

def replay():
    choice = input("Хотите играть дальше? Введите Y или N")
    return choice == 'Y'
