#chess notation to cordinate interperter
from chess_engine import*
#  x=a~h 0~7 y=8~1=0~7
def notation_to_cord(notation,turn,board):
    if notation=='O-O-O':
        if turn==1:
            return ['castling',28,24]
        else:
            return ['castling',4,0]
    elif notation=='O-O':
        if turn==1:
            return ['castling',28,31]
        else:
            return ['castling',4,7]
    if notation.find('=')!=-1:
        notation=notation[-1]+notation[:len(notation)-1]
    if notation.find('x')!=-1:
        notation.replace('x','')
    if notation.find('#')!=-1:
        notation.replace('#','')
    if notation.find('+')!=-1:
        notation.replace('+','')
    if notation[0]=="K":
        if notation[1].isalpha()!=1:
            notation.replace(notation[1],'')
        move=cordinate_change(notation[1:3])
        if turn==1:
            return ['move',28,move[0],move[1]]
        else:
            return ['move',4,move[0],move[1]]
    elif notation[0]=="Q" :
        if notation[1].isalpha()!=1:
            notation.replace(notation[1],'')
        move=cordinate_change(notation[1:3])
        pieces=[]
        if turn==1:
            for x in range(0,8):
                for y in range(0,8):
                    if board[y][x]==27 or (abs(board[y][x])>15and board[y][x])<0:
                        pieces.append(board[y][x])
        else:
            for x in range(0,8):
                for y in range(0,8):
                    if board[y][x]==4 or (abs(board[y][x])>15and board[y][x])<0:
                        pieces.append(board[y][x])
        pc=-1
        for piece in pieces:
            now=find(board,piece)
            if check(board,piece,now[0],now[1],move[0],move[1]):
                pc=piece
                break;
        return ['move',pc,move[0],move[1]]
    elif notation[0]=="B":
        move_x=-1
        if len(notation)>3:
            notation.replace(notation[1],'')

        move=cordinate_change(notation[1:3])
        pieces=[]
        if turn==1:
            if move_x==-1:
                for x in range(0,8):
                    for y in range(0,8):
                        if board[y][x]==26 or board[y][x]==29:
                            pieces.append(board[y][x])
            else:
                for y in range(0,8):
                    if board[y][move_x]==26 or board[y][move_x]==29:
                        pieces.append(board[y][x])
        else:
            pieces=[]
            if move_x==-1:
                for x in range(0,8):
                    for y in range(0,8):
                        if board[y][x]==2 or board[y][x]==5:
                            pieces.append(board[y][x])
            else:
                for y in range(0,8):
                    if board[y][move_x]==2 or board[y][move_x]==5:
                        pieces.append(board[y][x])
        pc=-1
        for piece in pieces:
            now=find(board,piece)
            if check(board,piece,now[0],now[1],move[0],move[1]):
                pc=piece
                break;
        return ['move',pc,move[0],move[1]]
    elif notation[0]=="N":
        move_x=-1
        if len(notation)>3:
            notation.replace(notation[1],'')
        move=cordinate_change(notation[1:3])
        pieces=[]
        if turn==1:
            if move_x==-1:
                for x in range(0,8):
                    for y in range(0,8):
                        if board[y][x]==25 or board[y][x]==30:
                            pieces.append(board[y][x])
            else:
                for y in range(0,8):
                    if board[y][move_x]==25 or board[y][move_x]==30:
                        pieces.append(board[y][x])
        else:
            pieces=[]
            if move_x==-1:
                for x in range(0,8):
                    for y in range(0,8):
                        if board[y][x]==1 or board[y][x]==6:
                            pieces.append(board[y][x])
            else:
                for y in range(0,8):
                    if board[y][move_x]==1 or board[y][move_x]==6:
                        pieces.append(board[y][x])
        pc=-1
        for piece in pieces:
            now=find(board,piece)
            if check(board,piece,now[0],now[1],move[0],move[1]):
                pc=piece
                break;
        return ['move',pc,move[0],move[1]]
    elif notation[0]=="R":
        move_x=-1
        if len(notation)>3:
            notation.replace(notation[1],'')
        move=cordinate_change(notation[1:3])
        pieces=[]
        if turn==1:
            if move_x==-1:
                for x in range(0,8):
                    for y in range(0,8):
                        if board[y][x]==24 or board[y][x]==31:
                            pieces.append(board[y][x])
            else:
                for y in range(0,8):
                    if board[y][move_x]==24 or board[y][move_x]==31:
                        pieces.append(board[y][x])
        else:
            pieces=[]
            if move_x==-1:
                for x in range(0,8):
                    for y in range(0,8):
                        if board[y][x]==0 or board[y][x]==7:
                            pieces.append(board[y][x])
            else:
                for y in range(0,8):
                    if board[y][move_x]==0 or board[y][move_x]==7:
                        pieces.append(board[y][x])
        pc=-1
        for piece in pieces:
            now=find(board,piece)
            if check(board,piece,now[0],now[1],move[0],move[1]):
                pc=piece
                break;
        return ['move',pc,move[0],move[1]]

    else:
        move_x=-1
        if len(notation)>2:
            notation.replace(notation[0],'')
        move=cordinate_change(notation[0:2])
        pieces=[]
        if turn==1:
            if move_x==-1:
                for x in range(0,8):
                    for y in range(0,8):
                        if board[y][x]>15 and board[y][x]<24:
                            pieces.append(board[y][x])
            else:
                for y in range(0,8):
                    if board[y][move_x]>15 and board[y][move_x]<24:
                        pieces.append(board[y][x])
        else:
            pieces=[]
            if move_x==-1:
                for x in range(0,8):
                    for y in range(0,8):
                        if board[y][x]>7 and board[y][x]<=15:
                            pieces.append(board[y][x])
            else:
                for y in range(0,8):
                    if board[y][move_x]>7 and board[y][move_x]<=15:
                        pieces.append(board[y][x])
        pc=-1
        for piece in pieces:
            now=find(board,piece)
            if check(board,piece,now[0],now[1],move[0],move[1]):
                pc=piece
                break;
        return ['move',pc,move[0],move[1]]
def cord_to_notation(piece,move_x,move_y):
    if piece==1 or piece==6:
        pc='N'
    elif piece==25 or piece==30:
        pc=='N'
    elif piece==2 or piece==5:
        pc=='B'
    elif piece==26 or piece==29:
        pc=='B'
    elif piece==0 or piece==7:
        pc=='R'
    elif piece==24 or piece==31:
        pc=='R'
    elif piece==3:
        pc=='Q'
    elif piece==27:
        pc=='Q'
    elif piece==4:
        pc=='K'
    elif piece==28:
        pc=='K'
    else:
        pc=''
    if move_x==0:
        x='a'
    elif move_x==1:
        x='b'
    elif move_x==2:
        x='c'
    elif move_x==3:
        x='d'
    elif move_x==4:
        x='e'
    elif move_x==5:
        x='f'
    elif move_x==6:
        x='g'
    elif move_x==7:
        x='h'
    y=8-move_y
    return pc+x+str(y)

def cordinate_change(string):
    result=[-1,-1]
    if string[0]=='a':
        result[0]=0
    elif string[0]=='b':
        result[0]=1
    elif string[0]=='c':
        result[0]=2
    elif string[0]=='d':
        result[0]=3
    elif string[0]=='e':
        result[0]=4
    elif string[0]=='f':
        result[0]=5
    elif string[0]=='g':
        result[0]=6
    elif string[0]=='h':
        result[0]=6
    result[1]=8-int(string[1])
    return result
"""
##test
board=[[32 for col in range(8)] for row in range(8)]
cnt=0
for y in range(0,8):
    for x in range(0,8):
        if cnt<16:
            board[y][x]=cnt
            cnt=cnt+1

        elif y>=6:
            board[y][x]=cnt
            cnt=cnt+1      
test=notation_to_cord('e4',1,board)
print(test)
print(cord_to_notation(test[1],test[2],test[3]))
"""