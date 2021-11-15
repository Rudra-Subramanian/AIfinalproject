import game1
import math


def convertHeuristic(heuristic):
    #player = 1 is from max value, player = -1 is from min value
    final = None
    for term in heuristic:
        if final == None:
            final = term[1] * getVariable(term[2])
        else:
            if(term[0] == '*'):
                final = final * (term[1] * getVariable(term[2]))
            if(term[0] == '+'):
                final = final + (term[1] * getVariable(term[2]))
            if(term[0] == '-'):
                final = final - (term[1] * getVariable(term[2]))
            if(term[0] == '/'):
                final = final / (term[1] * getVariable(term[2]))
    return(final)






def getVariable(variable):
    if(variable == 'x'):
        return(3) #replace for whatever the variable actually is
    elif(variable == 'y'):
        return(-1)
    else:
        return(4.6)

def maxValue(state, heuristic, depth):
    if(depth < 1):
        return([convertHeuristic(heuristic), None])
    elif(state.isTerminal()):
        return([state.value(), None]) #returns 1 if player 1 wins, -1 if player 2 wins
    else:
        best = [-2, None]
        move_list = state.getMoves()
        for move in move_list:
            value = minValue(state.nextState(move), heuristic, depth-1, player*-1)
            if value[0] > best[0]:
                best = [value[0], move]
        return best


def minValue(state, heuristic, depth):
    if(depth < 1):
        return([convertHeuristic(heuristic), None])
    elif(state.isTerminal()):
        return([state.value(), None]) #returns 1 if player 1 wins, -1 if player 2 wins
    else:
        best = [2, None]
        move_list = state.getMoves()
        for move in move_list:
            value = maxValue(state.nextState(move), heuristic, depth-1, player*-1)
            if value[0] < best[0]:
                best = [value[0], move]
        return best





def doMinimax(state, heuristic, player):
    if(player == 1):
        new_move = maxValue(state, heuristic, 2)
    elif(player == -1):
        new_move = minValue(state, heuristic, 2)
    return(new_move[1])









if __name__ == "__main__":
    print("Hello!")
