def display(list1):
    print("\n"*100)
    print("{}|{}|{}".format(list1[7],list1[8],list1[9]))
    print("----")
    print("{}|{}|{}".format(list1[4],list1[5],list1[6]))
    print("----")
    print("{}|{}|{}".format(list1[1],list1[2],list1[3]))
def players():
    player1=""
    player2=""
    while (player1 !="X" and player2 !="X"):
        player1=input("player 1 enter enter  X:O")
        if player1=="X":
            player2="O"
        else:
            player2="X"
    return (player1,player2)
def won(list1):
    if list1[7]==list1[8]==list1[9]=="X" or list1[7]==list1[4]==list1[1]=="X" or list1[7]==list1[5]==list1[3]=="X":
        re=list1[7]
    elif list1[8]==list1[5]==list1[2]=="X" or list1[4]==list1[5]==list1[6]=="X" or list1[9]==list1[5]==list1[1]=="X":
        re=list1[5]
    elif list1[3]==list1[6]==list1[9]=="X" or list1[3]==list1[2]==list1[1]=="X":
        re=list1[3]
    elif list1[7]==list1[8]==list1[9]=="O" or list1[7]==list1[4]==list1[1]=="O" or list1[7]==list1[5]==list1[3]=="O":
        re=list1[7]
    elif list1[8]==list1[5]==list1[2]=="O" or list1[4]==list1[5]==list1[6]=="O" or list1[9]==list1[5]==list1[1]=="O":
        re=list1[5]
    elif list1[3]==list1[6]==list1[9]=="O" or list1[3]==list1[2]==list1[1]=="O":
        re=list1[3]    
    else:
        re="i"  
    return re      

player1,player2=players()
print(player1)
print(player2)
list2=["#"," "," "," "," "," "," "," "," "," "]
i=1
while True:
    display(list2)
    a=int(input("enter player1 number"))
    list2[a]=player1
    display(list2)
    #print(won(list2))
    if won(list2)==player1:
        print("player 1 is win")
        break
    elif i==5:
        print("the match is draw")
        break

    b=int(input("enter player2 number"))
    list2[b]=player2
    display(list2)
    if won(list2)==player2:
        print("player 2 is win")
        break
    i=i+1



        




                
    
