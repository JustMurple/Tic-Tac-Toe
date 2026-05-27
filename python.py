def switch_player(p):
    if p==1:
        p=0
    else: p=1
    return p

def move(p):
    i,j=0,0
    print(p, "move")
    try: 
        m=int(input("Where do you want to move: "))
    except ValueError:
        print("Please enter an integer 1-9")
    if m<1 or 9<m:
        print("Invalid Move")
        return None
    
    if m<=3:
        i=0
    elif m<=6:
        i=1
    else: i=2
    
    if m%3==1: 
        j=0
    elif m%3==2:
        j=1
    else: j=2
    return [i,j]

def show(B):
    print(B[0][0], "|", B[0][1], "|", B[0][2])
    print(B[1][0], "|", B[1][1], "|", B[1][2])
    print(B[2][0], "|", B[2][1], "|", B[2][2])

def make_Move(p, B):
    val=move(p)
    x = True
    if val==None or B[val[0]][val[1]]!="-":
        x=False
    while x==False:
        val=move(p)
        if val!=None and B[val[0]][val[1]]=="-":
            x=True
    if p==1:
        B[val[0]][val[1]]="X"
    else: B[val[0]][val[1]]="O"

def check_Win(B):
    if B[0][0]==B[0][1]==B[0][2]!="-":
        return True
    elif B[1][0]==B[1][1]==B[1][2]!="-":
        return True
    elif B[2][0]==B[2][1]==B[2][2]!="-":
        return True
    elif B[0][0]==B[1][0]==B[2][0]!="-":
        return True
    elif B[0][1]==B[1][1]==B[2][1]!="-":
        return True
    elif B[0][2]==B[1][2]==B[2][2]!="-":
        return True
    elif B[0][0]==B[1][1]==B[2][2]!="-":
        return True
    elif B[0][2]==B[1][1]==B[2][0]!="-":
        return True
    else: return False

def check_Tie(B):
    for r in B:
        for c in r:
            if c=="-": return False
    return True
p=1

B = [["-","-","-"],
     ["-","-","-"],
     ["-","-","-"]]

show(B)

while not check_Win(B) and not check_Tie(B):
    make_Move(p, B)
    show(B)
    p=switch_player(p)

if check_Win(B):
    print(switch_player(p), "Won!")
else: print("It's a tie :(")