#!/usr/bin/python3.7

import random

lBaseBoard = [ ["| ", "| ", "| "], ["| ", "| ", "| "], ["| ", "| ", "| "]]
lBoard = [ ["| ", "| ", "| "], ["| ", "| ", "| "], ["| ", "| ", "| "]]
bTwoPlayer = False
bBotGoesFirst = False
def printBoard():
    global lBoard
    iCount = 1
    print(" 1 2 3 ")
    for lRow in lBoard:
        for sCell in lRow:
            print(sCell, end="")
        print("| "+str(iCount)+"\n")
        iCount += 1

def getBoardCopy(board):

    duplicateBoard = [[],[],[]]
    for x in range(3):
        for y in range(3):
            duplicateBoard[x].append(board[x][y])
    return duplicateBoard


def checkVictory(iRow, iColumn):
    global lBoard, lBaseBoard, sPlay, sBotGame, bTwoPlayer
    bSomeoneWon = False
    bSkipLoop = False
    if lBoard[0][iColumn] == lBoard[1][iColumn] == lBoard[2][iColumn]:
        bSomeoneWon = True
    elif lBoard[iRow][0] == lBoard[iRow][1] == lBoard[iRow][2]:
        bSomeoneWon = True
    elif iRow == iColumn and (lBoard[0][0] == lBoard[1][1] == lBoard[2][2]):
		#0,0 1,1 2,2
        bSomeoneWon = True
    elif iRow+iColumn == 2 and (lBoard[0][2] == lBoard[1][1] == lBoard[2][0]):
        #0,2 1,1 2,0
        bSomeoneWon = True

    if bSomeoneWon :
        bSkipLoop = True
        if lBoard[iRow][iColumn] == "|X":
            print("Player 1 (X) WON the game! Gratz")
        elif lBoard[iRow][iColumn] == "|O":
            print("Player 2 (O) WON the game! Gratz")

        sPlay = input("Play again? (yes/no): ")
        if(sPlay == "yes" or sPlay == "Yes"):
            sBotGame = input("Do you want to play with a bot? (yes/no): ")
            if(sBotGame == "Yes" or sBotGame == "yes"):
                bTwoPlayer = False
                bBotGoesFirst = botGoesFirst()
                if(bBotGoesFirst):
                    print("The bot goes first (x)")
                else:
                    print("You go first (x)")
            else:
                bTwoPlayer = True
            lBoard = getBoardCopy(lBaseBoard)
            printBoard()
    return bSkipLoop


def checkDraw():
    global lBoard, lBaseBoard, sPlay, sBotGame, bTwoPlayer
    bSkipLoop = False
    iFreeCells = 0
    for lRow in lBoard:
        for sCell in lRow:
            if sCell == "| ":
                iFreeCells += 1
    if iFreeCells == 0:
        bSkipLoop = True
        print("The table is full. It's a DRAW!")
        sPlay = input("Play again? (yes/no): ")
        if(sPlay == "yes" or sPlay == "Yes"):
            sBotGame = input("Do you want to play with a bot? (yes/no): ")
            if(sBotGame == "Yes" or sBotGame == "yes"):
                bTwoPlayer = False
                bBotGoesFirst = botGoesFirst()
                if(bBotGoesFirst):
                    print("The bot goes first (x)")
                else:
                    print("You go first (x)")
            else:
                bTwoPlayer = True
            lBoard = getBoardCopy(lBaseBoard)
            printBoard()
    #if 2 empty cells check neighbhours. check conditions
    return bSkipLoop

def playerOneTurn():
    global lBoard
    print("Player 1 turn (X)!")
    iRow = int(input("Enter Row:"))
    iColumn = int(input("Enter Column:"))

    if iRow >= 1 and iRow <= 3 and iColumn >= 1 and iColumn <= 3 and lBoard[iRow-1][iColumn-1] == "| ":
        lBoard[iRow-1][iColumn-1] = "|X"
        printBoard()
    else:
        print("Wrong move! Come Again.")
        playerOneTurn()
    bIWon = checkVictory(iRow-1,iColumn-1)
    if bIWon:
        return bIWon
    else:
        return checkDraw()

def playerTwoTurn():
    global lBoard
    print("Player 2 turn (O)!")
    iRow = int(input("Enter Row:"))
    iColumn = int(input("Enter Column:"))

    if iRow >= 1 and iRow <= 3 and iColumn >= 1 and iColumn <= 3 and lBoard[iRow-1][iColumn-1] == "| ":
        lBoard[iRow-1][iColumn-1] = "|O"
        printBoard()
    else:
        print("Wrong move! Come Again.")
        playerTwoTurn()
    bIWon = checkVictory(iRow-1,iColumn-1)
    if bIWon:
        return bIWon
    else:
        return checkDraw()

def victoryCheckForBot(lBoardCopy, iRow, iColumn, sMove):

    if(lBoardCopy[iRow][iColumn] != "| "):
        return False
    else:
        lBoardCopy[iRow][iColumn] = sMove
    if lBoardCopy[0][iColumn] == lBoardCopy[1][iColumn] == lBoardCopy[2][iColumn]:
        return True
    elif lBoardCopy[iRow][0] == lBoardCopy[iRow][1] == lBoardCopy[iRow][2]:
        return True
    elif iRow == iColumn and (lBoardCopy[0][0] == lBoardCopy[1][1] == lBoardCopy[2][2]):
		#0,0 1,1 2,2
        return True
    elif iRow+iColumn == 2 and (lBoardCopy[0][2] == lBoardCopy[1][1] == lBoardCopy[2][0]):
        #0,2 1,1 2,0
        return True
    else:
        return False

def makeBotMove(iRow, iColumn, sBotLetter):
    global lBoard
    print("The moved to the row: " + str(iRow+1) + " and the column: " + str(iColumn+1))
    lBoard[iRow][iColumn] = sBotLetter
    printBoard()
    bIWon = checkVictory(iRow,iColumn)
    if bIWon:
        return bIWon
    else:
        return checkDraw()

def botTurn(bBotGoesFirst):
    global lBoard
    if(bBotGoesFirst):
        sBotLetter = "|X"
        sPlayerLetter = "|O"
    else:
        sBotLetter = "|O"
        sPlayerLetter = "|X"

    bFound = False


    #check if we can win the next move
    for x in range(3):
        for y in range(3):
            lBoardCopy = getBoardCopy(lBoard)
            if(victoryCheckForBot(lBoardCopy, x, y, sBotLetter)):
                iRow = x
                iColumn = y
                bFound = True
                break
        if bFound:
            break


    #check if the player can win the next move
    if( not bFound):
        for x in range(3):
            for y in range(3):
                lBoardCopy = getBoardCopy(lBoard)
                if(victoryCheckForBot(lBoardCopy, x, y, sPlayerLetter)):
                    iRow = x
                    iColumn = y
                    bFound = True
                    break
            if bFound:
                break


    #take the opposite corner from the player
    if(not bFound):
        if(lBoard[0][0] == sPlayerLetter and lBoard[2][2] == "| "):
            iRow = 2
            iColumn = 2
            bFound = True
        elif(lBoard[2][2] == sPlayerLetter and lBoard[0][0] == "| " ):
            iRow = 0
            iColumn = 0
            bFound = True
        elif(lBoard[0][2] == sPlayerLetter and lBoard[2][0] == "| " ):
            iRow = 2
            iColumn = 0
            bFound = True
        elif(lBoard[2][0] == sPlayerLetter and lBoard[0][2] == "| " ):
            iRow = 0
            iColumn = 2
            bFound = True

    #take center if it's free
    if(not bFound):
        if(lBoard[1][1] == "| "):
            iRow = 1
            iColumn = 1
            bFound = True

    #take corners if they are free
    if (not bFound):
        if(lBoard[0][0] == "| "):
            iRow = 0
            iColumn = 0
            bFound = True
        elif(lBoard[0][2] == "| "):
            iRow = 0
            iColumn = 2
            bFound = True
        elif(lBoard[2][0] == "| "):
            iRow = 2
            iColumn = 0
            bFound = True
        elif(lBoard[2][2] == "| "):
            iRow = 2
            iColumn = 2
            bFound = True

    #if nothing works move to the sides
    if (not bFound):
        if(lBoard[0][1] == "| "):
            iRow = 0
            iColumn = 1
            bFound = True
        elif(lBoard[1][0] == "| "):
            iRow = 1
            iColumn = 0
            bFound = True
        elif(lBoard[1][2] == "| "):
            iRow = 1
            iColumn = 2
            bFound = True
        elif(lBoard[2][1] == "| "):
            iRow = 2
            iColumn = 1
            bFound = True

    return makeBotMove(iRow, iColumn, sBotLetter)

def botGoesFirst():
        if (random.randint(0,1) == 0):
            return True
        else:
            return False


printBoard()
sPlay = input("Do you want to play? (yes/no): ")
if(sPlay == "yes" or sPlay == "Yes"):
    sBotGame = input("Do you want to play with a bot? (yes/no): ")
    if(sBotGame == "Yes" or sBotGame == "yes"):
        bTwoPlayer = False
        bBotGoesFirst = botGoesFirst()
        if(bBotGoesFirst):
            print("The bot goes first (x)")
        else:
            print("You go first (x)")
    else:
        bTwoPlayer = True
while (sPlay == "yes" or sPlay == "Yes"):
    if(bTwoPlayer):
        if(playerOneTurn()):
            continue

        if(playerTwoTurn()):
            continue
    elif (bBotGoesFirst):
        if(botTurn(bBotGoesFirst)):
            continue
        if(playerTwoTurn()):
            continue
    else:
        if(playerOneTurn()):
            continue
        if(botTurn(bBotGoesFirst)):
            continue
