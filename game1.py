"""
game1.py
This module represents the game of Connect 4.

@author Bryce Wiedenbeck
@author Anna Rafferty (adapted from original)
@author Dave Musicant (further adapted for Python 3)
"""
import sys
import numpy as np
import minimax


HEIGHT = 6 # Height of the connect 4 board
WIDTH = 7 # Width of the connect 4 board
CONNECT = 4  # Number of items in a sequence necessary to win


class State(object):
    """
    Represents a Connect 4 board.
    """

    def __init__(self, state=None, move=None):
        """
        Constructor. Makes a copy of state if a
        state is passed in (i.e., non-destructive).
        """

        if state == None:
            self._board = np.zeros([HEIGHT, WIDTH], int)
            self._heights = np.zeros(WIDTH, int)
            self.turn = 1
        else:
            self._board = np.array(state._board)
            self._heights = np.array(state._heights)
            self.turn = -state.turn
        if move != None:
            self._board[HEIGHT - self._heights[move] - 1, move] = state.turn
            self._heights[move] += 1
        self.key = "".join(map(str, self._board.flat)) + str(self.turn)

    def getMoves(self):
        """
        Returns a vector of columns that one can place a piece in.
        """
        moves = np.nonzero(self._heights < HEIGHT)[0]
        np.random.shuffle(moves)
        return moves

    def nextState(self, move):
        """
        Returns the State that would result from taking move in this state.
        """
        return State(self, move)

    def isTerminal(self):
        """
        Returns True if one player has won or if there are no more moves (a draw).
        Otherwise, returns False.
        """
        if len(self.getMoves()) == 0:
            return True
        return self._wins(-1) or self._wins(1)

    def getTurn(self):
        """
        Returns +1 for the first player or -1 for the second player.
        This is the player whose turn it is to move in this state.
        """
        return self.turn

    def getKey(self):
        """
        Returns a string representing this state.
        """
        return self.key


    def value(self):
        """
        Returns 0 if the state is a draw or hasn't been
        won by anyone, returns 1 if it's a win for the first
        player (i.e., the first player just made a move that resulted
        in this state, which is a win for the first player), and
        returns -1 if it's a win for the second player.
        """
        if self._wins(1):
            return 1
        elif self._wins(-1):
            return -1
        return 0

    def _wins(self, player):
        """
        Returns True if this state is a win for the given player (1 = player 1, -1 = player 2) and False otherwise.
        """
        for j in range(WIDTH):#start from left
            for i in range(HEIGHT-1, -1, -1):#start from bottom
                if self._board[i,j] == player:
                    for k in range(1,CONNECT):#go up
                        if (i-k < 0) or (self._board[i-k, j] != player):
                            break
                        if k == CONNECT - 1:
                            return True
                    for k in range(1,CONNECT):#go right
                        if (j + k >= WIDTH) or (self._board[i, j+k] != player):
                            break
                        if k == CONNECT - 1:
                            return True
                    for k in range(1,CONNECT):#go up-right
                        if (i-k < 0) or (j + k >= WIDTH) or (self._board[i-k, j+k] != player):
                            break
                        if k == CONNECT - 1:
                            return True
            for i in range(HEIGHT-1, -1, -1):
                if self._board[i,j] == player:
                    for k in range(1,CONNECT):#go down-right
                        if (i + k >= HEIGHT) or (j + k >= WIDTH) or (self._board[i+k, j+k] != player):
                            break
                        if k == CONNECT - 1:
                            return True
        return False

def show_values(node):
    """
    Prints out the the board with a ranking of moves based on their values
    in MCTS. 1 is the move MCTS sees as the best move, and 8 is the worst
    move.
    """
    values = sorted(set([c.value for c in node.children.values()]))
    move_rank = {m:1+values.index(c.value) for m,c in node.children.items()}
    result = u"\n" + (" " + u"\u25a0")*WIDTH + u" \u25E9\n"
    for i in range(HEIGHT):
        result +=  u"\u25A1" + " "
        for j in range(WIDTH):
            move = j
            if i == (HEIGHT - node.state._heights[j] - 1) and move_rank.get(move, 10) < 10:
                c = str(move_rank[move])
            else:
                c = _print_char(node.state._board[i,j])
            result += c + " "
        result += u"\u25A1" + "\n"
    result += u"\u25EA" + (" " + u"\u25a0") * WIDTH
    return result

def print_board(state):
    """
    Print out the board in a human-readable form.
    """
    result = u"\n" + (" " + u"\u25a0")*WIDTH + u" \u25E9\n"
    for i in range(HEIGHT):
        result +=  u"\u25A1" + " "
        for j in range(WIDTH):
            c = _print_char(state._board[i,j])
            result += c + " "
        result += u"\u25A1" + "\n"
    result += u"\u25EA" + (" " + u"\u25a0") * WIDTH
    return result

def _print_char(i):
    """
    Get the unicode string to be printed for a piece of type i, or
    the character for an empty cell if i is 0. Note that 1 corresponds to a
    piece played by player 2 and -1 corresponds to a piece played by player 1
    (this is the opposite of how the turn instance variable works
    in state).
    """
    if i > 0:
        return u'\u25CB' # black piece
    if i < 0:
        return u'\u25CF' # white piece
    return u'\u00B7' # empty cell

def new_game():
    """
    Get a state representing a new game of Connect 4.
    """
    return State()


def debug():
#     moves = [7, 1, 2, 4, 7, 1, 1, 1, 7,2, 4, 1, 0, 2, 0, 2, 7, 1, 4, 2]
    moves = [7, 4, 5, 5, 6, 6, 7, 6, 7, 7]
    moves = [7, 5,4, 5, 6, 6, 7, 6, 7, 7]

    state = new_game()
    for moveNum, move in zip(range(len(moves)), moves):
        state = state.nextState(move)
        if moveNum == 16:
            print("last seven")
        print(print_board(state))
        print("is win player 1:", state._wins(1))
        print("is win player 2:", state._wins(-1))

def runGame(heuristic, depth, PLAYER1, PLAYER2):
    gameover = False
    maxMoves = WIDTH * HEIGHT
    state = new_game()
    while ((not gameover) and maxMoves > 0):
        print("current board \n")
        print(print_board(state))
        print("\n")
        if PLAYER1 == 'human':
            check = False
            while(check == False):
                print("where do you want to move. enter a number between 0 and " , WIDTH-1)
                print("\n")
                move = input()
                if (int(move) >= 0 and int(move) < WIDTH):
                    check = True
                else:
                    print("Invalid input")
        elif PLAYER1 == 'computer':
            move = minimax.doMinimax(state, heuristic, 1, depth)
        state = state.nextState(int(move))
        maxMoves = maxMoves - 1
        if(state.isTerminal()):
            gameover = True
            break
        print("current board \n")
        print(print_board(state))
        print("\n")
        if PLAYER2 == 'human':
            check = False
            while(check == False):
                print("where do you want to move. enter a number between 0 and " , WIDTH-1)
                print("\n")
                move = input()
                if (int(move) >= 0 and int(move) < WIDTH):
                    check = True
                else:
                    print("Invalid input")
        elif PLAYER2 == 'computer':
            move = minimax.doMinimax(state, heuristic, -1, depth)
        state = state.nextState(int(move))
        maxMoves = maxMoves - 1
        if(state.isTerminal()):
            gameover = True
            break
    print("\n the game has ended \n")
    print(state.value(), " has won\n")
    print(print_board(state))
    return([maxMoves, state.value(), state])

#runs the game with two computers (able to have mutliple heuristics)
def runComputerGame(heuristic, depth, PLAYER1Heuristic, PLAYER2Heuristic):
    gameover = False
    maxMoves = WIDTH * HEIGHT
    state = new_game()
    while ((not gameover) and maxMoves > 0):
        move = minimax.doMinimax(state, PLAYER1Heuristic, 1, depth)
        state = state.nextState(int(move))
        maxMoves = maxMoves - 1
        if(state.isTerminal()):
            gameover = True
            break
        move = minimax.doMinimax(state, PLAYER2Heuristic, -1, depth)
        state = state.nextState(int(move))
        maxMoves = maxMoves - 1
        if(state.isTerminal()):
            gameover = True
            break
    return([maxMoves, state.value(), state])










if __name__ == "__main__":
    heuristic = [["*",0.015, "x"], ["+",0, "y"], ["-",0, "z"], ["+",00, "v"]]
    depth = sys.argv[3]
    if sys.argv[1] == "human":
        player1con = 'human'
    else:
        player1con = 'computer'
    if sys.argv[2] == 'human':
        player2con = 'human'
    else:
        player2con = 'computer'
    winner = runGame(heuristic, int(depth), player1con, player2con)
    print(winner)
