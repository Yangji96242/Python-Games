x=0
y=0

#defs////////////////////////////////////////////////////

#input direction
def ToPosition():
    go(input("please enter position (N/S/W/E):"),step=1)

#move to position:
def go(position,step=1):
    global x
    global y
    if position.upper() in ["N","S","W","E"]:
        if position.upper()=="N":
            y+=step
        elif position.upper()=="S":
            y-=step
        elif position.upper()=="W":
            x-=step
        else:
            x+=step
        locked(position)
        print("you are in ({},{}) right now.".format(x,y))
        ToPosition()
    else:
        print("wrong input")
        print("you are in ({},{}) right now.".format(x,y))
        ToPosition()

#locked room
def locked(position):
    if x==1 and y==1:
        notice(position)
    elif x==2 and y==2:
        notice(position)
        
def notice(position):
        print("Ops...the room is locked.")
        NoEntry(position)   

#No entry
def NoEntry(position):
    global x
    global y
    if position.upper()=="N":
        y-=1
    elif position.upper()=="S":
        y+=1
    elif position.upper()=="W":
        x=+1
    else:
        x-=1
        



#the main////////////////////////////////////////////////
ToPosition()

#this is test git
#this is test git2
#this is test git3
#this is test git4
#dev 1
#feature 1
