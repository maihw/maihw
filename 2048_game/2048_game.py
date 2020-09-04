import curses
from random import randrange, choice
from collections import defaultdict
actions = ['Up', 'Left', 'Down', 'Right', 'Restart', 'Exit']
letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']
actions_dict = dict(zip(letter_codes, actions * 2))

def main(stdscr):

    def init():
        '''初始化游戏棋盘'''
        return 'Game'

    def not_game(state):
        '''展示游戏结束界面。
        读取用户输入得到action，判断是重启游戏还是结束游戏
        '''
        responses = defaultdict(lambda:state)
        responses['Restart'], responses['Exit'] = 'Init', 'Exit'
        return responses[action]

    def game():
        '''画出当前棋盘状态
        读取用户输入得到action
        '''
        if action == 'Restart':
            return 'Init'
        if action == 'Exit':
            return 'Exit'
            if 游戏胜利了:
                return 'Win'
            if 游戏失败了:
                return 'Gameover'
        return 'Game'

    state_actions = {
            'Init': init,
            'Win': lambda: not_game('Win'),
            'Gameover': lambda: not_game('Gameover'),
            'Game': game
    }
    state = 'Init'
    while state != 'Exit':
        state = state_actions[state]()

def get_user_action(keyboard):
    char = 'N'
    while char not in actions_dict:
        char = keyboard.getch()
    return actions_dict[char]


class GameField(object):
    def __init__(self, height=4, width=4, win=2048):
        self.height = height
        self.width = width
        self.win_value = 2048
        self.highscore = 0
        self.reset()

def spawn(self):
    new_element = 4 if randrange(100) > 89 else 2
    (i,j) = choice([(i,j) for i in range(self.width) for j in range
        (self.height) if self.field[i][j] == 0])
    self.field[i][j] = new_element

def reset(self):
    if self.score > self.highscore:
        self.highscore = self.score
    self.score = 0
    self.field = [[0 for i in range(self.width)] for j in range(self.height)]
    self.spawn()
    self.spawn()

def move_row_left(row):
    def tighten(row):
        '''把零散的非零单元挤到一块'''
        new_row = [i for i in row if i != 0]
        new_row += [0 for i in range(len(row) - len(new_row))]
        return new_row
    def merge(row):
        '''对邻近元素进行合并'''
        pair = False
        new_row = []
        for i in range(len(row)):
            if pair:
                new_row.appen(2 * row[i])
                self.score += 2 * row[i]
                apir = False
            else:
                if i + 1 < len(row) and row[i] == row[i + 1]:
                    pair = True
                    new_row.append(0)
                else:
                    new_row.append(row[i])
        assert len(new_row) == len(row)
        return new_row
    return tighten(merge(tighten(row)))

def transpose(field):
    return [list(row) for row in zip(*field)]

def invert(field):
    return [row[::-1] for row in field]

def move(self, direction):
    moves = {}
    moves['Left'] = lambda field:
        [move_row_left(row) for row in field]
    moves['Right'] = lambda field:
        invert(moves['Left'](invert(field)))
    moves['Up'] = lambda field:
        transpose(moves['Left'](transpose(field)))
    moves['Down'] = lambda field:
        transpose(moves['Right'](transpose(field)))
    if direction in moves:
        if self.move_is_possible(direction):
            self.field = moves[direction](self.field)
            self.spawn()
            return True
        else:
            return False

def is_win(self):
    return any(any(i >= self.win_value for i in row) for row in self.field)

def is_gameover(self):
    return not any(self.move_is_possible(move) for move in actions)

