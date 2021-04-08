from random import* 
from chess_engine import*
import numpy as np
board=[[32 for col in range(8)] for row in range(8)]


#q_data=np.load("E:\chess_ai_data\\test3.npy")

q_data=np.zeros((17,8,8,17,8,8,32,8,8))
cnt=0
print("start")
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
penalty=0
point=0
white_previous=[16,0,0]
black_previous=[16,0,0]
turn=True
while True:
    if gamecount>1000:
        break;
    if white!=[]:
        white_previous=[white[len(white)-1][6]-16,white[len(white)-1][7],white[len(white)-1][8]]
    if black!=[]:
        black_previous=[black[len(black)-1][6],black[len(black)-1][7],black[len(black)-1][8]]
    if turn:
        piece_h=16
        e_b=-1
        e_w=1
    else:
        piece_h=0
        e_b=1
        e_w=-1
    bests=[]
    for piece in range(piece_h,piece_h+16):
        now=find(board,abs(piece))
        for x in range(0,8):
            if now[0]==-1:
                break;
            for y in range(0,8):
                if check(board,piece,now[0],now[1],x,y):
                    """
                    bests.append([piece,x,y,q_data[white_previous[0],white_previous[1],white_previous[2],black_previous[0],black_previous[1],black_previous[2],piece,x,y]])
                    """
                    bests.append([piece,x,y])
                    
    """
    bests.sort(key=lambda x:x[3])
    bests.reverse()
    best_index=bests[0]
    """
    best_index=choice(bests)
    
    reward=move(board,best_index[0],best_index[1],best_index[2])
    if turn:
        white.append([white_previous[0],white_previous[1],white_previous[2],black_previous[0],black_previous[1],black_previous[2],best_index[0],best_index[1],best_index[2]])
    else:
        black.append([white_previous[0],white_previous[1],white_previous[2],black_previous[0],black_previous[1],black_previous[2],best_index[0],best_index[1],best_index[2]])
    if reward>=0:
        point=point+1
        if reward==0:
            penalty=penalty+1
        else:
            penalty=0
    if penalty<50:
        for i in range(len(white)-1,-1,-1):
            q_data[white[i][0],white[i][1],white[i][2],white[i][3],white[i][4],white[i][5],white[i][6],white[i][7],white[i][8]]=q_data[white[i][0],white[i][1],white[i][2],white[i][3],white[i][4],white[i][5],white[i][6],white[i][7],white[i][8]]+reward*e_w
            e_w=e_w/1.1
        for i in range(len(black)-1,-1,-1):
            q_data[black[i][0],black[i][1],black[i][2],black[i][3],black[i][4],black[i][5],black[i][6],black[i][7],black[i][8]]=q_data[black[i][0],black[i][1],black[i][2],black[i][3],black[i][4],black[i][5],black[i][6],black[i][7],black[i][8]]+reward*e_b
            e_b=e_b/1.1
    else:
        for i in range(len(white)-1,-1,-1):
            q_data[white[i][0],white[i][1],white[i][2],white[i][3],white[i][4],white[i][5],white[i][6],white[i][7],white[i][8]]=q_data[white[i][0],white[i][1],white[i][2],white[i][3],white[i][4],white[i][5],white[i][6],white[i][7],white[i][8]]-1
        for i in range(len(black)-1,-1,-1):
            q_data[black[i][0],black[i][1],black[i][2],black[i][3],black[i][4],black[i][5],black[i][6],black[i][7],black[i][8]]=q_data[black[i][0],black[i][1],black[i][2],black[i][3],black[i][4],black[i][5],black[i][6],black[i][7],black[i][8]]-1
    if reward==-1:
        print('miss')
        gameover=1
    elif reward>=1000:
        gameover=1
        if turn:
            print('white win!')
        else:
            print('black win!')
    turn=not(turn)
    if gameover==1 or point>300:
        turn=True
        gameover=0
        gamecount=gamecount+1
        print(white)
        print(black)
        white=[]
        black=[]
        print(gamecount)
        print(best_index)
        print(point)
        point=0
        white_previous=[16,0,0]
        black_previous=[16,0,0]
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
                elif board[y][x]==27:
                    print('Q',end=" ")
                elif board[y][x]==4:
                    print('k',end=" ")
                elif board[y][x]==28:
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




    
np.save("E:\chess_ai_data\\test3",q_data) 