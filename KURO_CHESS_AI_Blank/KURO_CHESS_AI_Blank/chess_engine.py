#chess engine for q learning ai
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
        elif die_piece==3 or die_piece==27:
            return 9
        elif die_piece==4 or die_piece==28:
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
    elif piece==27:
        return queen_check(board,now_x,now_y,move_x,move_y,-1)
    elif piece==4:
        return king_check(board,now_x,now_y,move_x,move_y,1)
    elif piece==28:
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
                check_x=move_x+1
                check_y=move_y+1
                while check_x!=now_x and check_y!=now_y:
                    if board[check_y][check_x]!=32:
                        break;
                    check_x=check_x+1
                    check_y=check_y+1
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

def piece_exist(board,x,y):
    if board[y][x]!=32:
        return abs(board[y][x])
    else:
        return -1
def read_field(board):
    field_index=[0,0,0,0]
    for y in range(0,8):
        for x in range(0,8):
            if board[y][x]!=32:
                field_index[int(y/2)]=field_index[int(y/2)]+1
    return field_index


