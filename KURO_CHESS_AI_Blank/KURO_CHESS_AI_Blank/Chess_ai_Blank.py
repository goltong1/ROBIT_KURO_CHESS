import numpy as np
from random import*
def move(board,piece,move_x,move_y):
    cordinate=find(board,piece)
    now_x=cordinate[0]
    now_y=cordinate[1]
    if move_x>7 or move_x<0 or move_y>7 or move_y<0:
        return -1
    if check(board,piece,now_x,now_y,move_x,move_y):
        board[now_y][now_x]=32
        die_piece=board[move_y][move_x]
        if (piece>7 and piece<=15 and move_y==7) or (piece>15 and piece<24 and move_y==0):
            piece=piece*-1
        board[move_y][move_x]=piece
        if 7<die_piece and die_piece<24:
            return 1
        elif die_piece==1 or die_piece==6 or die_piece==25 or die_piece==30:
            return 3
        elif die_piece==2 or die_piece==5 or die_piece==26 or die_piece==29:
            return 3
        elif die_piece==0 or die_piece==7 or die_piece==24 or die_piece==31:
            return 5
        elif die_piece==3 or die_piece==28:
            return 9
        elif die_piece==4 or die_piece==27:
            return 1000
        else:
            return 0

    else:
        return -1
    
def check(board,piece,now_x,now_y,move_x,move_y):
    if now_x==-1 or (now_x==move_x and now_y==move_y)or move_x>7 or move_y>7:
        return 0
    elif piece>7 and piece<=15:
        if board[now_y][now_x]>=0:
            return pawn_check(board,now_x,now_y,move_x,move_y,1) #블랙 1, 화이트 -1
        else:
            return queen_check(board,now_x,now_y,move_x,move_y,1)
    elif piece>15 and piece<24:
        if board[now_y][now_x]>=0:
            return pawn_check(board,now_x,now_y,move_x,move_y,-1)
        else:
            return queen_check(board,now_x,now_y,move_x,move_y,-1)
    elif piece==1 or piece==6:
        return knight_check(board,now_x,now_y,move_x,move_y,1)
    elif piece==25 or piece==30:
        return knight_check(board,now_x,now_y,move_x,move_y,-1)
    elif piece==2 or piece==5:
        return bishop_check(board,now_x,now_y,move_x,move_y,1)
    elif piece==26 or piece==29:
        return bishop_check(board,now_x,now_y,move_x,move_y,-1)
    elif piece==0 or piece==7:
        return rook_check(board,now_x,now_y,move_x,move_y,1)
    elif piece==24 or piece==31:
        return rook_check(board,now_x,now_y,move_x,move_y,-1)
    elif piece==3:
        return queen_check(board,now_x,now_y,move_x,move_y,1)
    elif piece==28:
        return queen_check(board,now_x,now_y,move_x,move_y,-1)
    elif piece==4:
        return king_check(board,now_x,now_y,move_x,move_y,1)
    elif piece==27:
        return king_check(board,now_x,now_y,move_x,move_y,-1)
    else:
        return 0
def pawn_check(board,now_x,now_y,move_x,move_y,WB): 
    if WB*(move_y-now_y)==1 and abs(move_x-now_x)==0 and board[move_y][move_x]>=32:
        return 1
    elif WB*(move_y-now_y)==1 and abs(move_x-now_x)==1:
        if WB==1:
            if board[move_y][move_x]>15 and board[move_y][move_x]<32:
                return 1
        else:
            if board[move_y][move_x]<16 and board[move_y][move_x]>=0:
                return 1
    elif move_y-now_y==2 and abs(move_x-now_x)==0 and board[move_y][move_x]>=32 and now_y==1 and board[move_y-1][move_x]>=32:
        return 1
    elif now_y-move_y==2 and abs(move_x-now_x)==0 and board[move_y][move_x]>=32 and now_y==6 and board[move_y+1][move_x]>=32:
        return 1
    else:
        return 0
def knight_check(board,now_x,now_y,move_x,move_y,WB):
    if (abs(move_y-now_y)==2 and abs(move_x-now_x)==1) or (abs(move_y-now_y)==1 and abs(move_x-now_x)==2):
        if board[move_y][move_x]>=32:
            return 1
        elif WB==1:
            if board[move_y][move_x]>15 and board[move_y][move_x]<32:
                return 1
        else:
            if board[move_y][move_x]<16 and board[move_y][move_x]>=0:
                return 1
    else:
        return 0

def bishop_check(board,now_x,now_y,move_x,move_y,WB):
    if abs(move_y-now_y)==abs(move_x-now_x):
        if board[move_y][move_x]==32 or (WB==1 and board[move_y][move_x]>15 and board[move_y][move_x]<32) or (WB==-1 and board[move_y][move_x]<16 and board[move_y][move_x]>=0):
            check_x=move_x
            check_y=move_y
            if move_x>now_x and move_y>now_y:
                check_x=move_x-1
                check_y=move_y-1
                while check_x!=now_x and check_y!=now_y:
                    if board[check_y][check_x]!=32:
                        break;
                    check_x=check_x-1
                    check_y=check_y-1
            elif move_x<now_x and move_y>now_y:
                check_x=move_x+1
                check_y=move_y-1
                while check_x!=now_x and check_y!=now_y:
                    if board[check_y][check_x]!=32:
                        break;
                    check_x=check_x+1
                    check_y=check_y-1
            elif move_x>now_x and move_y<now_y:
                check_x=move_x-1
                check_y=move_y+1
                while check_x!=now_x and check_y!=now_y:
                    if board[check_y][check_x]!=32:
                        break;
                    check_x=check_x-1
                    check_y=check_y+1
            elif move_x<now_x and move_y<now_y:
                check_x=move_x-1
                check_y=move_y-1
                while check_x!=now_x and check_y!=now_y:
                    if board[check_y][check_x]!=32:
                        break;
                    check_x=check_x-1
                    check_y=check_y-1
            if check_x==now_x and check_y==now_y:
               return 1
            else:
               return 0
        else:
            return 0
    else:
        return 0

def rook_check(board,now_x,now_y,move_x,move_y,WB):
    if (abs(move_y-now_y)>0 and abs(move_x-now_x)==0) or (abs(move_y-now_y)==0 and abs(move_x-now_x)>0) :
        if board[move_y][move_x]==32 or (WB==1 and board[move_y][move_x]>15 and board[move_y][move_x]<32) or (WB==-1 and board[move_y][move_x]<16 and board[move_y][move_x]>=0):
            check_x=move_x
            check_y=move_y
            if move_y-now_y>0:
                check_y=move_y-1
                while check_y!=now_y:
                    if board[check_y][check_x]!=32:
                        break;
                    check_y=check_y-1
                if check_y==now_y:
                    return 1
                else:
                    return 0
            elif move_y-now_y<0:
                check_y=move_y+1
                while check_y!=now_y:
                    if board[check_y][check_x]!=32:
                        break;
                    check_y=check_y+1
                if check_y==now_y:
                    return 1
                else:
                    return 0
            elif move_x-now_x>0:
                check_x=move_x-1
                while check_x!=now_x:
                    if board[check_y][check_x]!=32:
                        break;
                    check_x=check_x-1
                if check_x==now_x:
                    return 1
                else:
                    return 0
            elif move_x-now_x<0:
                check_x=move_x+1
                while check_x!=now_x:
                    if board[check_y][check_x]!=32:
                        break;
                    check_x=check_x+1
                if check_x==now_x:
                    return 1
                else:
                    return 0
            else:
                return 0
        else:
            return 0
    else:
        return 0
            
def queen_check(board,now_x,now_y,move_x,move_y,WB):
    return rook_check(board,now_x,now_y,move_x,move_y,WB) or bishop_check(board,now_x,now_y,move_x,move_y,WB)
def king_check(board,now_x,now_y,move_x,move_y,WB):
    if board[move_y][move_x]==32 or (WB==1 and board[move_y][move_x]>15 and board[move_y][move_x]<32) or (WB==-1 and board[move_y][move_x]<16 and board[move_y][move_x]>=0):
        if (abs(move_x-now_x)==1 and abs(move_y-now_y)==1) or (abs(move_x-now_x)==1 and abs(move_y-now_y)==0) or (abs(move_x-now_x)==0 and abs(move_y-now_y)==1):
            return 1
        else:
            return 0
    else:
        return 0
def find(board,piece):
    result=[-1,-1]
    for y in range(0,8):
        for x in range(0,8):
            if abs(board[y][x])==piece:
                result[0]=x
                result[1]=y
                return result

    return result
def read_field(board):
    field_index=[0,0,0,0]
    for y in range(0,8):
        for x in range(0,8):
            if board[y][x]!=32:
                field_index[int(y/2)]=field_index[int(y/2)]+1
    return field_index

board=[[32 for col in range(8)] for row in range(8)]

#q_data=np.zeros((17,17,17,17,32,8,8))
q_data=np.load("test1.npy")

cnt=0

for y in range(0,8):
    for x in range(0,8):
        if cnt<16:
            board[y][x]=cnt
            cnt=cnt+1
        elif y>=6:
            board[y][x]=cnt
            cnt=cnt+1      



gamecount=0
white=[]
black=[]
gameover=0
while True:
 
    if gamecount>100000:
        break;
    field_index=read_field(board)
    for piece in range(16,32):
        for x in range(0,8):
            if find(board,piece)[0]==-1:
                break;
            for y in range(0,8):
                if piece==16 and x==0 and y==0:
                    best=q_data[field_index[0],field_index[1],field_index[2],field_index[3],piece,0,0]
                    bests=[]
                    bests.append([piece,x,y])
                elif q_data[field_index[0],field_index[1],field_index[2],field_index[3],piece,x,y]>best:
                    best=q_data[field_index[0],field_index[1],field_index[2],field_index[3],piece,x,y]
                    bests=[]
                    bests.append([piece,x,y])
                elif q_data[field_index[0],field_index[1],field_index[2],field_index[3],piece,x,y]==best:
                    bests.append([piece,x,y])
    best_index=choice(bests)
    white.append([field_index[0],field_index[1],field_index[2],field_index[3],best_index[0],best_index[1],best_index[2]])
    reward=move(board,best_index[0],best_index[1],best_index[2])
    if reward==-1:
        q_data[field_index[0],field_index[1],field_index[2],field_index[3],best_index[0],best_index[1],best_index[2]]=q_data[field_index[0],field_index[1],field_index[2],field_index[3],best_index[0],best_index[1],best_index[2]]-9999
        gameover=1
    else:
        e=1
        for i in range(len(white)-1,-1,-1):
            q_data[white[i][0],white[i][1],white[i][2],white[i][3],white[i][4],white[i][5],white[i][6]]=q_data[white[i][0],white[i][1],white[i][2],white[i][3],white[i][4],white[i][5],white[i][6]]+reward*e
            e=e/10
        e=1
        for i in range(len(black)-1,-1,-1):
            q_data[black[i][0],black[i][1],black[i][2],black[i][3],black[i][4],black[i][5],black[i][6]]=q_data[black[i][0],black[i][1],black[i][2],black[i][3],black[i][4],black[i][5],black[i][6]]-reward*e
            e=e/10
        if reward>=1000:
            gameover=1
        else:
            field_index=read_field(board)
            for piece in range(0,16):
                for x in range(0,8):
                    if find(board,piece)[0]==-1:
                        break;
                    for y in range(0,8):
                        if piece==0 and x==0 and y==0:
                            best=q_data[field_index[0],field_index[1],field_index[2],field_index[3],piece,0,0]
                            bests=[]
                            bests.append([piece,x,y])
                        elif q_data[field_index[0],field_index[1],field_index[2],field_index[3],piece,x,y]>best:
                            best=q_data[field_index[0],field_index[1],field_index[2],field_index[3],piece,x,y]
                            bests=[]
                            bests.append([piece,x,y])
                        elif q_data[field_index[0],field_index[1],field_index[2],field_index[3],piece,x,y]==best:
                            bests.append([piece,x,y])
            best_index=choice(bests)
            black.append([field_index[0],field_index[1],field_index[2],field_index[3],best_index[0],best_index[1],best_index[2]])
            reward=move(board,best_index[0],best_index[1],best_index[2])
            if reward==-1:
                q_data[field_index[0],field_index[1],field_index[2],field_index[3],best_index[0],best_index[1],best_index[2]]=q_data[field_index[0],field_index[1],field_index[2],field_index[3],best_index[0],best_index[1],best_index[2]]-9999
                gameover=1
            else:
                e=1
                for i in range(len(white)-1,-1,-1):
                    q_data[white[i][0],white[i][1],white[i][2],white[i][3],white[i][4],white[i][5],white[i][6]]=q_data[white[i][0],white[i][1],white[i][2],white[i][3],white[i][4],white[i][5],white[i][6]]+reward*e
                    e=e/10
                e=1
                for i in range(len(black)-1,-1,-1):
                    q_data[black[i][0],black[i][1],black[i][2],black[i][3],black[i][4],black[i][5],black[i][6]]=q_data[black[i][0],black[i][1],black[i][2],black[i][3],black[i][4],black[i][5],black[i][6]]-reward*e
                    e=e/10
                if reward>=1000:
                    gameover=1
    if gameover==1:
        gameover=0
        gamecount=gamecount+1
        #print(white)
        #print(black)
        white=[]
        black=[]
        print(gamecount)
        print(best_index)
        field_index=read_field(board)
        print(field_index)
        
        for y in range(0,8):
            for x in range(0,8):
                if abs(board[y][x])>7 and abs(board[y][x])<=15:
                    if board[y][x]>=0:
                        print('p',end=" ")
                    else:
                        print('q',end=" ")
                elif abs(board[y][x])>15 and abs(board[y][x])<24:
                    if board[y][x]>=0:
                        print('P',end=" ")
                    else:
                        print('Q',end=" ")
                elif board[y][x]==1 or board[y][x]==6:
                    print('n',end=" ")
                elif board[y][x]==25 or board[y][x]==30:
                    print('N',end=" ")
                elif board[y][x]==2 or board[y][x]==5:
                    print('b',end=" ")
                elif board[y][x]==26 or board[y][x]==29:
                    print('B',end=" ")
                elif board[y][x]==0 or board[y][x]==7:
                    print('r',end=" ")
                elif board[y][x]==24 or board[y][x]==31:
                    print('R',end=" ")
                elif board[y][x]==3:
                    print('q',end=" ")
                elif board[y][x]==28:
                    print('Q',end=" ")
                elif board[y][x]==4:
                    print('k',end=" ")
                elif board[y][x]==27:
                    print('K',end=" ")
                else:
                    print('0',end=" ")
                
            print("")
        
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




    
np.save("test1",q_data) 




