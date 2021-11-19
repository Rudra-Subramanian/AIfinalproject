import game1
import math


def convertHeuristic(heuristic, state):
    #player = 1 is from max value, player = -1 is from min value
    final = None


    for term in heuristic:
        if final == None:
            final = term[1] * getVariable(term[2], state)
        else:
            if(term[0] == '*'):
                final = final * (term[1] * getVariable(term[2], state))
            if(term[0] == '+'):
                final = final + (term[1] * getVariable(term[2], state))
            if(term[0] == '-'):
                final = final - (term[1] * getVariable(term[2], state))
            if(term[0] == '/'):
                final = final / (term[1] * getVariable(term[2], state))
    #print("heuristic : ", final)
    return(final)






def getVariable(variable, state):
    if(variable == 'x'): 
        middle_of_board = []
        x = (game1.WIDTH-1) / 2
        sums = 0
        if (x - int(x) == 0):
            middle_of_board.append(int(x))
        else:
            middle_of_board.append(int(math.ceil(x)))
            middle_of_board.append(int(x))
        for middles in middle_of_board:
            height = game1.HEIGHT - 1
            while height >= 0:
                sums = sums + state._board[middles,height]
                height = height - 1
        return(sums)


    elif(variable == 'y'):
        sums = 0
        for i in range(game1.WIDTH- 1):
            sums = sums - state._board[i,game1.HEIGHT - 1]
        return(sums)
    elif(variable == 'z'):
        sums = 0
        for i in range(game1.WIDTH - 1):
            sums = sums + state._board[i,0]
        return(sums)
    elif(variable == 'v'):
        sums = 0
        for i in range(game1.HEIGHT - 3):
            sums = sums - state._board[5,i]
        return(sums)
    else:
        return(-0.3)

def maxValue(state, heuristic, depth, player):
    if(depth < 1):
        return([convertHeuristic(heuristic, state), None])
    elif(state.isTerminal()):
        return([state.value(), None]) #returns 1 if player 1 wins, -1 if player 2 wins
    else:
        best = [-2, None]
        move_list = state.getMoves()
        for move in move_list:
            value = minValue(state.nextState(move), heuristic, depth-1, player*-1)
            if value[0] > best[0]:
                best = [value[0], move]
        #print("max value: ", best)
        return best


def minValue(state, heuristic, depth, player):
    if(depth < 1):
        return([convertHeuristic(heuristic, state), None])
    elif(state.isTerminal()):
        #print("terminal state value: ", state.value())
        return([state.value(), None]) #returns 1 if player 1 wins, -1 if player 2 wins
    else:
        best = [2, None]
        move_list = state.getMoves()
        for move in move_list:
            value = maxValue(state.nextState(move), heuristic, depth-1, player*-1)
            if value[0] < best[0]:
                best = [value[0], move]
        #print("min value: ", best)
        return best





def doMinimax(state, heuristic, player, depth):
    if(player == 1):
        new_move = maxValue(state, heuristic, depth, 1)
    elif(player == -1):
        new_move = minValue(state, heuristic, depth, -1)
    return(new_move[1])









if __name__ == "__main__":
    print("Hello!")
