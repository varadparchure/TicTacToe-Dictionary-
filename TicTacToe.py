    
#sys.sys.sys
#GIT_varad
#user-ADMIN__9651-[VARADPARCHURE]
    
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']    
   
   
#1->win
#2->draw
#3-> running


Win = 1    
Draw = -1    
Running = 0    
Stop = 1    
key = "X"
###########################    

Game = Running   
#player
p=1 


#This Function Draws Game Board    
def DrawBoard():
    print("\n")
    print(board[1] + "  |" + board[2] +"  |"  +board[3])    
    print("___|___|___")       
    
    print(board[4] + "  |" + board[5] +"  |"  +board[6])    
    print("___|___|___")       
    
    print(board[7] + "  |" + board[8] +"  |"  +board[9])    
    print("   |   |   ")      
    

def CheckPosition(x):    
    if(board[int(x)] == ' '):    
        return True    
    else:    
        return False  
    
def gameplay():    
    global Game    
    #Horizontal winning condition    
    if(board[1] == board[2] and board[2] == board[3] and board[1] != ' '):    
        Game = Win   
    elif(board[4] == board[5] and board[5] == board[6] and board[4] != ' '):    
        Game = Win     
    elif(board[7] == board[8] and board[8] == board[9] and board[7] != ' '):    
        Game = Win 
        
        
        
    #Vertical Winning Condition    
    elif(board[1] == board[4] and board[4] == board[7] and board[1] != ' '):    
        Game = Win     
    elif(board[2] == board[5] and board[5] == board[8] and board[2] != ' '):    
        Game = Win     
    elif(board[3] == board[6] and board[6] == board[9] and board[3] != ' '):    
        Game=Win 
        
    #Diagonal Winning Condition    
    elif(board[1] == board[5] and board[5] == board[9] and board[5] != ' '):    
        Game = Win     
    elif(board[3] == board[5] and board[5] == board[7] and board[5] != ' '):    
        Game=Win   
        
        
        
    #Match Tie or Draw Condition    
    elif(board[1]!=' ' and board[2]!=' ' and board[3]!=' ' and 
         board[4]!=' ' and board[5]!=' ' and board[6]!=' ' and 
         board[7]!=' ' and board[8]!=' ' and board[9]!=' '):    
        
        Game=Draw  
    else:            
        Game=Running
        
 
print("\nPLAYER 1-> X   &   PLAYER 2-> O\n*******************************")

while(Game==Running):
    
    DrawBoard()
    if(p % 2 != 0):
        print("\nPlayer 1s chance\n")
        key= "X"
    else:
        print("\nPlayer 2s chance\n")
        key= "O"
 
    
    choice=int(input("\n Enter any position form 1-9 \n"))

    if(CheckPosition(choice)):
        board[int(choice)]=key
        p=p+1
        gameplay()

    
DrawBoard()
if(Game==Draw):    
    print("Game Draw")    
elif(Game==Win):    
    p-=1    
    if(p%2!=0):    
        print("Player 1 Won")    
    else:    
        print("Player 2 Won")    



















       
        
        
