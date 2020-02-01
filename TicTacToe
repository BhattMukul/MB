'''This Program Is For TIC TAC TOE Game
Build Tic Tac Toe In Very Basic and Easy Way'''

def winner():
    '''This function is Used To Check The Winner'''
    global result
    global count
    global l1
    global l2
    global l3
    #l4(just below) is the the lis of all the winning conditions for this Game 
    l4=[[l1[0],l2[0],l3[0]],[l1[1],l2[1],l3[1]],[l1[2],l2[2],l3[2]],[l1[0],l1[1],l1[2]],[l2[0],l2[1],l2[2]],[l3[0],l3[1],l3[2]],[l1[0],l2[1],l3[2]],[l1[2],l2[1],l3[0]]]
    if count >=5: #it should be atleast Total 5 moves after which the winner should be checked 
        for l in l4:
            if l[0]==l[1]==l[2] and l[0]!=' ':
                result="WINNER"
                if l[0]=="X":
                    print("PLAYER 1 WON, Congo...")
                elif l[0]=="O":
                    print("PLAYER 2 WON, Congo...")
    





def fun_OX(sym,index):
    ''' This Function Is To Enter The X and O at the provided Position by the players'''
    global pos
    global l1
    global l2
    global l3
    bpos=pos.pop(index) #To Get The Position Number From The List [pos](can be seen below)
    if bpos==1 :
        l1[0]=sym
    elif bpos==2 :
        l1[1]=sym
    elif bpos==3 :       #these all the the condition to enter X and O at given Position
        l1[2]=sym
    elif bpos==4 :
        l2[0]=sym
    elif bpos==5 :
        l2[1]=sym
    elif bpos==6 :
        l2[2]=sym
    elif bpos==7 :
        l3[0]=sym
    elif bpos==8 :
        l3[1]=sym
    elif bpos==9 :
        l3[2]=sym
    print(l1)
    print(l2)   # These are to print the Game Board After Every Move 
    print(l3)
    print("----------------------------------------------")
    winner()



print("----Let's Play TIC TAC TOE----\n")
print('''Player 1 --> "X"
Player 2 --> "O"''')

print('''Here Is Board Structure
['1','2','3']
['4','5','6']
['7','8','9']
Here 1-9 Are The Positions Of The Places Where You Both Want To Insert "X" & "O"
''')
l1=[' ',' ',' ']
l2=[' ',' ',' ']    #Game Board
l3=[' ',' ',' ']
pos=[1,2,3,4,5,6,7,8,9] #Position List
area=None
index=None
result=" "
count=0   #number of moves Done
for x in range(1,10): #These Are All The Condion So that Players Can Go ONE BY ONE
    if x%2!=0 :
        area = int(input("Player 1 : Enter The Pos No.: "))
        if area in pos:
            index=pos.index(area)
            count+=1
            fun_OX("X",index)
        else:
            print("Wrong Input")
    else:
        area = int(input("Player 2 : Enter The Pos No.: "))
        if area in pos:
            index=pos.index(area)
            count += 1
            fun_OX("O", index)
        else:
            print("Wrong Input")
    if count==9 and result==' ':
        print("Game Over, IT's A DRAW") #condition for DRAW
        break
    if result != " ":
        break    #break if someone won before 9 moves
    

