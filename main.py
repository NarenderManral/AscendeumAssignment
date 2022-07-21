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
            
        temp= playersPos[i]
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


