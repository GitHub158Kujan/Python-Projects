import random
board = [" " for _ in range(9)]
currentplayer="X"
secplayer="O"
winner=None
gameRunning=True

#print the board
def gameboard(board) :
    print(" "+board[0]+" | "+board[1]+" | "+board[2])
    print("----------")
    print(" "+board[3]+" | "+board[4]+" | "+board[5])
    print("----------")
    print(" "+board[6]+" | "+board[7]+" | "+board[8])
  

#take input 
def playerinput(board):
    inp=int(input("First player: Enter position :"))
    if inp>=1 and inp<=9 and board[inp-1]==" ":
        board[inp-1]=currentplayer
    else:
        print("Oops player is already in that spot!")
        playerinput(board)
        
def playerinput2(board):
    inp2=int(input("Second player: Enter position :"))
    if inp2>=1 and inp2<=9 and board[inp2-1]==" ":
        board[inp2-1]=secplayer
    else:
        print("Oops player is already in that spot!")
        playerinput2(board)
        
#check for win or tie
def checkHorizonatal(board):
    global winner
    if board[0]==board[1]==board[2] and board[1]!=" " :
        winner=board[0]
        return True
    elif board[3]==board[4]==board[5] and board[3]!=" " : 
        winner=board[3]
        return True
    elif board[6]==board[7]==board[8] and board[6]!=" " : 
        winner=board[6]
        return True 
    return False
    
def checkVertical(board):
     global winner
     if board[0]==board[3]==board[6] and board[0]!=" " :
        winner=board[0]
        return True
     elif board[1]==board[4]==board[7] and board[1]!=" " : 
        winner=board[1]
        return True
     elif board[2]==board[5]==board[8] and board[2]!=" " : 
        winner=board[2]
        return True 
     return False   
    
def checkDiag(board):
      global winner
      if board[0]==board[4]==board[8] and board[0]!=" " :
        winner=board[0]
        return True
      elif board[6]==board[4]==board[2] and board[6]!=" " : 
        winner=board[6]
        return True 
      return False
    
def checkTie(board):
    if " " not in board:
        gameboard(board)
        print("It is a tie!")
        return True
    return False  
def checkWin():
    if checkHorizonatal(board) or checkVertical(board) or checkDiag(board): 
        print(f"The winner is {winner}")  
        return True  
    return False        

#switch player
def switchPlayer():
    global currentplayer
    if currentplayer == "X":
        secplayer = "O"
    else:
        secplayer = "X"
        
def switchPlayerComputer():
    global currentplayer
    if currentplayer == "X":
        currentplayer = "O"
    else:
        currentplayer = "X"
         
#computer
def computer(board):
    while currentplayer=="O":
        position=random.randint(0,8)  
        if board[position]==" ":
            board[position]="O"
            switchPlayerComputer() 
            break 
               

print("------TIC TAC TOE GAME-----")               
print("Press C: If you want to play with computer: ")
print("Press F: If you want to play with friend: ")
sel=input()   
     
#Run the program
while gameRunning:
    if sel == 'F' or sel == 'f':
       gameboard(board)
       playerinput(board)
       if checkWin() or checkTie(board):
            gameRunning = False
            gameboard(board)
            break
       gameboard(board)
       switchPlayer() 
       playerinput2(board)
       if checkWin() or checkTie(board):
            gameRunning = False
            gameboard(board)
            break
    elif sel == 'C' or sel == 'c':
       gameboard(board)
       playerinput(board)  
       if checkWin() or checkTie(board):
           gameRunning = False
           gameboard(board)
           break
       switchPlayerComputer() 
       computer(board)
       if checkWin() or checkTie(board):
           gameRunning = False
           gameboard(board)
           break