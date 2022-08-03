
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
#print("Hello world")
import random
print("Enter the grid size")
n = int(input())
playersCurPos = [0,0,0,0]
playersPos = [[],[],[],[]]
xCoordinate = []
yCoordinate = []
playersCur = [0,0,0,0]
flag = 0;
diceRollHistory = [[],[],[],[]]
win = False;
winner = -1;
for i in range(n):
    if flag == 0:
        for j in range(n):
            xCoordinate  += [j]
            yCoordinate += [i]
        flag = 1;
    elif flag == 1:
        for j in range(n):
            xCoordinate += [n - j -1]
            yCoordinate += [i]
        flag = 0
            
#for i in range(n*n):
#    print(xCoordinate[i])
#print("END --------------------")
#for i in range(n*n):  
#    print(yCoordinate[i])

while(win==False):
    for i in range(4):
        dice = random.randint(1,6)
        diceRollHistory[i] = diceRollHistory[i] + [dice]
        temp = playersPos[i]
        if(len(temp)==0):
            playersPos[i] = temp + [dice]
        elif((playersPos[i][len(temp)-1]+dice) > n*n):
            playersPos[i] = temp + [playersPos[i][len(temp)-1]]
        else:
            playersPos[i] = temp + [playersPos[i][len(temp)-1]+dice]
        playersCur[i] = playersPos[i][len(temp)-1]
        
        if(xCoordinate[playersCur[i]] == yCoordinate[playersCur[i]]):
            pass
        else if(i!=0 && (xCoordinate[playersCur[i]] == yCoordinate[playersCur[0]]) && (xCoordinate[playersCur[0]] == yCoordinate[playersCur[i]])):
            playersCur[0][len(playersCur[0])-1]= 0
            playersPos[0][len(playersCur[0])-1] = 0
        else if((i!=1 && xCoordinate[playersCur[i]] == yCoordinate[playersCur[1]] && xCoordinate[playersCur[1]] == yCoordinate[playersCur[i]])):
            playersCur[1][len(playersCur[1])-1]= 0
            playersPos[1][len(playersCur[1])-1] = 0
        else if( (i!=2 && xCoordinate[playersCur[i]] == yCoordinate[playersCur[2]] && xCoordinate[playersCur[2]] == yCoordinate[playersCur[i]])):
            playersCur[1][len(playersCur[1])-1]= 0
            playersPos[1][len(playersCur[1])-1] = 0
        elif((i!=3 && xCoordinate[playersCur[i]] == yCoordinate[playersCur[3]] && xCoordinate[playersCur[3]] == yCoordinate[playersCur[i]])):
            playersCur[1][len(playersCur[1])-1]=  0
            playersPos[1][len(playersCur[1])-1] = 0
        elif( (i!=0 && playersCur[i]==playersCur[0]) || (i!=1 && playersCur[i]==playersCur[1]) || (i!=2 && playersCur[i]==playersCur[2]) || (i!=3 && playersCur[i]==playersCur[2] ) ):
            playersCur[i][len(playersCur[i])-1]=  0
            playersPos[i][len(playersCur[i])-1] = 0
        
        if(playersPos[i][len(temp)-1] == n*n):
            win=True
            winner = i;
            break;

print("Winner is Player:"+str(winner+1))
print("Player No",end="   ")
print("Dice Rolled ",end="     ")
print("Player Position history",end="    ")
print("Player Postion X Y coordinate ",end="   ")
print("Is player winner")
for i in range(4):
    print(str(i+1),end="            ")
    print(diceRollHistory[i],end="    ")
    print(playersPos[i],end="           ")
    for j in range(len(playersPos[i])):
        #print("The player position history is "+str(playersPos[i][j]))
        #print("The player x coordinate is " + str(xCoordinate[playersPos[i][j] - 1]))
        #print("The player y coordinate is " + str(yCoordinate[playersPos[i][j] - 1]))
        print("("+  str(xCoordinate[playersPos[i][j] - 1])+","+str(yCoordinate[playersPos[i][j] - 1]) + ")",end=" ")
    print("      ",end="  ")
    if(i==winner):
        print("Yes        ")
    else:
        print("No         ")
        
    #print("------------------------------------")
    #print("------------------------------------")
