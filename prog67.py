def generateMoves(color, board):
    ''' This function takes 2 arguments as parameters. It takes color and the current board of the game and then returns the list of possible moves that the certain color pawn can make'''

    listOfmoves = []                                                        # Creats an empty list
    import copy
    newboard = copy.deepcopy(board)
    for row in range(len(board)):
        for col in range(len(board)):
            if color == 1:                                                  # Moves for the white pawn
                if newboard[row][col] == color: # checks for my pawns
                    if row+1 <= (len(board)-1):                             # Restriction that the pawn does not go out of the board's bounds
                        if newboard[row+1][col] == 0:                       # expression for the pawn to move straight down
                            newboard = copy.deepcopy(board)
                            newboard[row+1][col] = newboard[row][col]
                            newboard[row][col] = 0
                            listOfmoves.append(newboard)
                    if col <= 1 :
                        if row+1 <= (len(board)-1):
                            if newboard[row+1][col+1] == 2:                 # takes down black pawn by moving diagonally right
                               newboard = copy.deepcopy(board)
                               newboard[row+1][col+1] = newboard[row][col]
                               newboard[row][col] = 0
                               listOfmoves.append(newboard)
                    if col >= 1:
                        if row+1 <= (len(board)-1):
                            if newboard[row+1][col-1] == 2:                 # takes down black pawn by moving diagnally left
                               newboard = copy.deepcopy(board)
                               newboard[row+1][col-1] = newboard[row][col]
                               newboard[row][col] = 0
                               listOfmoves.append(newboard)

            if color == 2:                                                  # Moves for the black pawn
                if newboard[row][col] == color:
                    if newboard[row-1][col] == 0:                           # Moves straight top if empty space
                        newboard = copy.deepcopy(board)
                        newboard[row-1][col] = newboard[row][col]
                        newboard[row][col] = 0
                        listOfmoves.append(newboard)
                    if col >= 1:
                        if newboard[row-1][col-1] == 1:                     # Takes down white pawn by moving diagnally left
                           newboard = copy.deepcopy(board)
                           newboard[row-1][col-1] = newboard[row][col]
                           newboard[row][col] = 0
                           listOfmoves.append(newboard)
                    if col <= 1:
                        if newboard[row-1][col+1] == 1:                     # takes down white pawn by moving diagnally right
                           newboard = copy.deepcopy(board)
                           newboard[row-1][col+1] = newboard[row][col]
                           newboard[row][col] = 0
                           listOfmoves.append(newboard)

    return listOfmoves                  # returns the appended list from each case


def chooseBestMoves(color, mlist):
    ''' This function takes in the 2 arguments; color and possible moves from the generate moves and returns the best choice for the move we can play'''
    for possibleMove in  mlist:
        count1 = 0
        count2 = 0
        for board in possibleMove:
            j = 0
            for pawn in board:
                if pawn == color:
                    count1 = count1 +1             # counts either black or white pawns
                if pawn != color and pawn != 0:
                    count2 = count2 + 1                # counts either black or white pawns


                if j == 2 and pawn == color:       # chooses the option where pawn can go to the farthest row and win, rather than take down some other opponent
                    return possibleMove
            j = j+1

        # Chooses the option where each pawn takes down the other color
        if count1 > count2:
            return possibleMove
    # Chooses an option when both pawns cant take down wach other
    if count1 == count2:
        return possibleMove
