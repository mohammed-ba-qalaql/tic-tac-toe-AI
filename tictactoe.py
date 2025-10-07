"""
Tic Tac Toe Player
"""
import random
import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x=0
    o=0
    for i in range(3):
        for j in range(3):
            if board[i][j] == "X":
                x+=1
            elif board[i][j] == "O":
                o+=1
    if x > o :
        return "O"
    else:
        return "X"


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_set = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions_set.add((i,j))
    return actions_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action[0] < 0 or action[1] < 0 or action[0] > 2 or action[1] > 2:
        raise ValueError("None cought")
    play = player(board)
    deepCopy = copy.deepcopy(board)
    if deepCopy[action[0]][action[1]] == EMPTY:
        deepCopy[action[0]][action[1]] = play
        return deepCopy
    else:
        raise ValueError("action not valid")


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if check_winner(board,"X"):
        return "X"
    elif check_winner(board,"O"):
        return "O"
    else: 
        return None

def check_winner(board, player):
    return (
        board[0][0] == board[0][1] == board[0][2] == player or#
        board[1][0] == board[1][1] == board[1][2] == player or#
        board[2][0] == board[2][1] == board[2][2] == player or#
        board[0][0] == board[1][0] == board[2][0] == player or#
        board[0][1] == board[1][1] == board[2][1] == player or#
        board[0][2] == board[1][2] == board[2][2] == player or#
        board[0][0] == board[1][1] == board[2][2] == player or
        board[0][2] == board[1][1] == board[2][0] == player
    )


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    
    if not any(n == EMPTY for n in board[0]) and not any(n == EMPTY for n in board[1]) and not any(n == EMPTY for n in board[2]):
        return True
    
    return False



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    state = winner(board)
    if state == "X":
        return 1
    elif state == "O":
        return -1
    else :
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    stack = []
    checked = []
    checkedVal = []
    stack += actions(board)
    playing = player(board)
    value = None
    if terminal(board):
        return None
    if playing == "X":
        v = -1000
        while stack:
            move = stack.pop()
            result1 = result(board,move)
            value = minValue(result1)
            checked.append((move,value))
            checkedVal.append(value)

            v = max(v,value)
            if v == 1:
                return move
        maxVal = []
        for i in range(len(checked)):
            if checked[i][1] == max(checkedVal):
                maxVal.append(i)
        return checked[random.choice(maxVal)][0]
    else:
        v = 1000
        while stack:
            move = stack.pop()
            result1 = result(board,move)
            value = maxValue(result1)
            checked.append((move,value))
            checkedVal.append(value)
            v = min(v,value)
            if v == -1:
                return move
            
        minVal = []
        for i in range(len(checked)):
            if checked[i][1] == min(checkedVal):
                minVal.append(i)
        return checked[random.choice(minVal)][0]
    

def maxValue(board): 
    stack = []
    if terminal(board):
        return utility(board)
    v = -1000
    stack += actions(board)
    while stack:
        v = max(v,minValue(result(board,stack.pop())))
    return v
        
def minValue(board):
    stack = []
    if terminal(board):
        return utility(board)
    v = 1000
    stack += actions(board)
    while stack:
        v = min(v,maxValue(result(board,stack.pop())))
    return v