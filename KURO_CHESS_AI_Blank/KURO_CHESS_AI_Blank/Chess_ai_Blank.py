import numpy as np
from random import*
from chess_engine import*
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


point=0
while True:
    if gamecount>1000:
        break;
    field_index=read_field(board)
    for piece in range(16,32):
        if piece==16:
            best=best=q_data[field_index[0],field_index[1],field_index[2],field_index[3],piece,0,0]
            bests=[]
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
                """
                if q_data[field_index[0],field_index[1],field_index[2],field_index[3],piece,x,y]>-9999:
                    bests.append([piece,x,y])
                    """
    best_index=choice(bests)
    white.append([field_index[0],field_index[1],field_index[2],field_index[3],best_index[0],best_index[1],best_index[2]])
    reward=move(board,best_index[0],best_index[1],best_index[2])
    """
    while reward==-1:
        q_data[field_index[0],field_index[1],field_index[2],field_index[3],best_index[0],best_index[1],best_index[2]]=q_data[field_index[0],field_index[1],field_index[2],field_index[3],best_index[0],best_index[1],best_index[2]]-99999
        best_index=choice(bests)
        reward=move(board,best_index[0],best_index[1],best_index[2])
        if reward==-1:
            bests.remove(best_index)
            if bests==[]:
                break;
    """
    if reward==-1:
        q_data[field_index[0],field_index[1],field_index[2],field_index[3],best_index[0],best_index[1],best_index[2]]=q_data[field_index[0],field_index[1],field_index[2],field_index[3],best_index[0],best_index[1],best_index[2]]-99999
        gameover=1
    else:
        if reward>=0:
            point=point+1
        e=1
        for i in range(len(white)-1,-1,-1):
            q_data[white[i][0],white[i][1],white[i][2],white[i][3],white[i][4],white[i][5],white[i][6]]=q_data[white[i][0],white[i][1],white[i][2],white[i][3],white[i][4],white[i][5],white[i][6]]+reward*e
            e=e/10
        e=1
        for i in range(len(black)-1,-1,-1):
            q_data[black[i][0],black[i][1],black[i][2],black[i][3],black[i][4],black[i][5],black[i][6]]=q_data[black[i][0],black[i][1],black[i][2],black[i][3],black[i][4],black[i][5],black[i][6]]-reward*e
            e=e/10
        if reward>=1000:
            print("white win!")
            gameover=1
            break;
        else:
            field_index=read_field(board)
            for piece in range(0,16):
                if piece==0:
                    best=best=q_data[field_index[0],field_index[1],field_index[2],field_index[3],piece,0,0]
                    bests=[]
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
                        """
                        if q_data[field_index[0],field_index[1],field_index[2],field_index[3],piece,x,y]>-9999:
                            bests.append([piece,x,y])
                        """

            best_index=choice(bests)
            black.append([field_index[0],field_index[1],field_index[2],field_index[3],best_index[0],best_index[1],best_index[2]])
            reward=move(board,best_index[0],best_index[1],best_index[2])
            """
            while reward==-1:
                q_data[field_index[0],field_index[1],field_index[2],field_index[3],best_index[0],best_index[1],best_index[2]]=q_data[field_index[0],field_index[1],field_index[2],field_index[3],best_index[0],best_index[1],best_index[2]]-99999
                best_index=choice(bests)
                reward=move(board,best_index[0],best_index[1],best_index[2])
                if reward==-1:
                    bests.remove(best_index)
                    if bests==[]:
                        break;
            """
            if reward==-1:
                q_data[field_index[0],field_index[1],field_index[2],field_index[3],best_index[0],best_index[1],best_index[2]]=q_data[field_index[0],field_index[1],field_index[2],field_index[3],best_index[0],best_index[1],best_index[2]]-99999
                gameover=1
            else:
                if reward>=0:
                    point=point+1
                e=1
                for i in range(len(white)-1,-1,-1):
                    q_data[white[i][0],white[i][1],white[i][2],white[i][3],white[i][4],white[i][5],white[i][6]]=q_data[white[i][0],white[i][1],white[i][2],white[i][3],white[i][4],white[i][5],white[i][6]]-reward*e
                    e=e/10
                e=1
                for i in range(len(black)-1,-1,-1):
                    q_data[black[i][0],black[i][1],black[i][2],black[i][3],black[i][4],black[i][5],black[i][6]]=q_data[black[i][0],black[i][1],black[i][2],black[i][3],black[i][4],black[i][5],black[i][6]]+reward*e
                    e=e/10
                    
                if reward>=1000:
                    print("black win!")
                    gameover=1
                    break;
                    
    if gameover==1 or point>500:
        point=0
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




    
np.save("test1",q_data) 




