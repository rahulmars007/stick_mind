
print("""
  ------------------------------------------------------
 |======================================================| 
 |============ WELCOME TO STRETEGY GAME ================|
 |============ DEVELOPED BY RAHUL MARS  ================|
 |======================================================|
  ------------------------------------------------------
   """)
t=21
A=input("ENTER PLAYER 1 NAME ")
B=input("ENTER PLAYER 2 NAME ")
def readMove():
    while(True):
        n=int(input("PLEASE ENTER NUMBER B/W 1 to 4 ="))
        if(n<1 or n>4):
            continue
        if(n>t):
            continue
        return n
while(True):
       print("TURN IS",A)
       a=readMove()
       if(1<=a<=4):
            t=t-a
            print("TOTAL STICK",t)
            if(t==0):
                print(A, "YOU LOSS") 
                print(B,"YOU WIN")
                print("AGAIN PLAY PRESS 1 AND EXIT FOR 0")
                x=int(input("ENTER NUMBER  "))
                if(x==1):
                    t=21
                    continue
                if(x==0):
                    break     
       print("TURN IS",B)
       b=readMove()
       if(1<=b<=4):
           t=t-b
           print("TOTAL STICK",t)
           if(t==0):
                print(B,"YOU LOSS")
                print(A, "YOU WIN")
                print("AGAIN PLAY PRESS 1 AND EXIT PRESS 0")
                x=int(input("ENTER NUMBER "))
                if(x==1):
                    t=21
                    continue
                if(x==0):
                    break 
        
      
        