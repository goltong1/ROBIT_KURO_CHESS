from chess_engine import*
import numpy as np
from random import*
import copy

q_data=np.load("E:\chess_ai_data\\test3.npy")
#q_data=np.zeros((17,8,8,17,8,8,32,8,8))
def find_best_move(board,turn,n,white_p,black_p):
    if turn:
        piece_h=16
    else:
        piece_h=0
    cases=[]
    for piece in range(piece_h,piece_h+16):
        now=find(board,abs(piece))
        for x in range(0,8):
            if now[0]==-1:
                break;
            for y in range(0,8):
                if check(board,piece,now[0],now[1],x,y):
                    cases.append([piece,x,y])
    best=-10000
    bests=[]
    for case in cases:
        tmp_board=copy.deepcopy(board)
        reward=move(tmp_board,case[0],case[1],case[2])
        if n%2==0 and reward>=5:
            return case
        elif n%2==1 and reward>100:
            return case
        if n<3:
            next_best=find_best_move(tmp_board,not(turn),n+1,white_p,black_p)
            reward=reward-move(tmp_board,next_best[0],next_best[1],next_best[2])
        if reward>best:
            best_index=case
            best=reward
            bests=[]
            bests.append(case)
        elif reward==best:
            bests.append(case)
    q_bests=[]
    if best==0:
        if n==1:
            for data in bests:
                q_bests.append([data[0],data[1],data[2],q_data[white_p[0],white_p[1],white_p[2],black_p[0],black_p[1],black_p[2],data[0],data[1],data[2]]])
            q_bests.sort(key=lambda x:x[3])
            q_bests.reverse()
            best_index=q_bests[0]
        else:
            best_index=choice(bests)
    if n==1:
        print(best)
    return best_index
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
done=False
turn=True
clicked=False
now_x=0
now_y=0
move_x=0
move_y=0
white_previous=[16,0,0]
black_previous=[16,0,0]
white=[]
black=[]
gamecount=0
gameover=0
count=0
print('white Turn')
while True:
    if gamecount>3:
        break;
    if white!=[]:
        white_previous=[white[len(white)-1][6]-16,white[len(white)-1][7],white[len(white)-1][8]]
    if black!=[]:
        black_previous=[black[len(black)-1][6],black[len(black)-1][7],black[len(black)-1][8]]
    if turn:
        e_b=-1
        e_w=1
        if count<3:
            best=find_best_move(board,turn,3,white_previous,black_previous)
        else:
            best=find_best_move(board,turn,1,white_previous,black_previous)
        reward=move(board,best[0],best[1],best[2])
        count=count+1
        white.append([white_previous[0],white_previous[1],white_previous[2],black_previous[0],black_previous[1],black_previous[2],best[0],best[1],best[2]])
        turn=False
        if reward>=1000:
            print("white win!")
            gameover=1
        print('black Turn')
                    
    else:
        e_b=1
        e_w=-1
        if count<4:
            best=find_best_move(board,turn,3,white_previous,black_previous)
        else:
            best=find_best_move(board,turn,1,white_previous,black_previous)
        reward=move(board,best[0],best[1],best[2])
        count=count+1
        black.append([white_previous[0],white_previous[1],white_previous[2],black_previous[0],black_previous[1],black_previous[2],best[0],best[1],best[2]])
        if reward>=1000:
            print('black win!')
            gameover=1
        turn=True
        print('white Turn')
    for i in range(len(white)-1,-1,-1):
        q_data[white[i][0],white[i][1],white[i][2],white[i][3],white[i][4],white[i][5],white[i][6],white[i][7],white[i][8]]=q_data[white[i][0],white[i][1],white[i][2],white[i][3],white[i][4],white[i][5],white[i][6],white[i][7],white[i][8]]+reward*e_w
        e_w=e_w/5
    for i in range(len(black)-1,-1,-1):
        q_data[black[i][0],black[i][1],black[i][2],black[i][3],black[i][4],black[i][5],black[i][6],black[i][7],black[i][8]]=q_data[black[i][0],black[i][1],black[i][2],black[i][3],black[i][4],black[i][5],black[i][6],black[i][7],black[i][8]]+reward*e_b
        e_b=e_b/5
    if gameover==1 or count>300:
        turn=True
        gameover=0
        gamecount=gamecount+1
        print(white)
        print(black)
        white=[]
        black=[]
        print(gamecount)
        print(count)
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