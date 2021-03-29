import numpy as np
from random import*
from chess_engine import*
board=[[32 for col in range(8)] for row in range(8)]


#q_data=np.load("E:\chess_ai_data\\test2.npy")
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
point=0
white_previous=[16,0,0]
black_previous=[16,0,0]
while True:
    if gamecount>5000:
        break;
    if white!=[]:
        white_previous=[white[len(white)-1][6]-16,white[len(white)-1][7],white[len(white)-1][8]]
    if black!=[]:
        black_previous=[black[len(black)-1][6],black[len(black)-1][7],black[len(black)-1][8]]
    for piece in range(16,32):
        if piece==16:
            best=q_data[white_previous[0],white_previous[1],white_previous[2],black_previous[0],black_previous[1],black_previous[2],piece,0,0]
            bests=[]
        for x in range(0,8):
            if find(board,piece)[0]==-1:
                break;
            for y in range(0,8):
                
                if piece==16 and x==0 and y==0:
                    best=q_data[white_previous[0],white_previous[1],white_previous[2],black_previous[0],black_previous[1],black_previous[2],piece,0,0]
                    bests=[]
                    bests.append([piece,x,y])
                elif q_data[white_previous[0],white_previous[1],white_previous[2],black_previous[0],black_previous[1],black_previous[2],piece,x,y]>best:
                    best=q_data[white_previous[0],white_previous[1],white_previous[2],black_previous[0],black_previous[1],black_previous[2],piece,x,y]
                    bests=[]
                    bests.append([piece,x,y])
                elif q_data[white_previous[0],white_previous[1],white_previous[2],black_previous[0],black_previous[1],black_previous[2],piece,x,y]==best:
                    bests.append([piece,x,y])
                """
                if q_data[white_previous[0],white_previous[1],white_previous[2],black_previous[0],black_previous[1],black_previous[2],piece,x,y]>-99999:
                    bests.append([piece,x,y])
                """
    best_index=choice(bests)
    reward=move(board,best_index[0],best_index[1],best_index[2])
    
    while reward==-1:
        bests.remove(best_index)
        if bests==[]:
            print('miss')
            break;
        q_data[white_previous[0],white_previous[1],white_previous[2],black_previous[0],black_previous[1],black_previous[2],best_index[0],best_index[1],best_index[2]]=q_data[white_previous[0],white_previous[1],white_previous[2],black_previous[0],black_previous[1],black_previous[2],best_index[0],best_index[1],best_index[2]]-99999
        best_index=choice(bests)
        reward=move(board,best_index[0],best_index[1],best_index[2])

    
    if reward==-1:
        q_data[white_previous[0],white_previous[1],white_previous[2],black_previous[0],black_previous[1],black_previous[2],best_index[0],best_index[1],best_index[2]]=q_data[white_previous[0],white_previous[1],white_previous[2],black_previous[0],black_previous[1],black_previous[2],best_index[0],best_index[1],best_index[2]]-99999
        gameover=1
    else:
        white.append([white_previous[0],white_previous[1],white_previous[2],black_previous[0],black_previous[1],black_previous[2],best_index[0],best_index[1],best_index[2]])
        if reward>=0:
            point=point+1
        e=1
        for i in range(len(white)-1,-1,-1):
            q_data[white[i][0],white[i][1],white[i][2],white[i][3],white[i][4],white[i][5],white[i][6],white[i][7],white[i][8]]=q_data[white[i][0],white[i][1],white[i][2],white[i][3],white[i][4],white[i][5],white[i][6],white[i][7],white[i][8]]+reward*e
            e=e/10
        e=1
        for i in range(len(black)-1,-1,-1):
            q_data[black[i][0],black[i][1],black[i][2],black[i][3],black[i][4],black[i][5],black[i][6],black[i][7],black[i][8]]=q_data[black[i][0],black[i][1],black[i][2],black[i][3],black[i][4],black[i][5],black[i][6],black[i][7],black[i][8]]-reward*e
            e=e/10
        if reward>=1000:
            print("white win!")
            gameover=1
            #break;
        else:
            if white!=[]:
                white_previous=white[len(white)-1]
            if black!=[]:
                black_previous=black[len(black)-1]
            field_index=read_field(board)
            for piece in range(0,16):
                if piece==0:
                    best=q_data[white_previous[0],white_previous[1],white_previous[2],black_previous[0],black_previous[1],black_previous[2],piece,0,0]
                    bests=[]
                for x in range(0,8):
                    if find(board,piece)[0]==-1:
                        break;
                    for y in range(0,8):
                        
                        if piece==0 and x==0 and y==0:
                            best=q_data[white_previous[0],white_previous[1],white_previous[2],black_previous[0],black_previous[1],black_previous[2],piece,0,0]
                            bests=[]
                            bests.append([piece,x,y])
                        elif q_data[white_previous[0],white_previous[1],white_previous[2],black_previous[0],black_previous[1],black_previous[2],piece,x,y]>best:
                            best=q_data[white_previous[0],white_previous[1],white_previous[2],black_previous[0],black_previous[1],black_previous[2],piece,x,y]
                            bests=[]
                            bests.append([piece,x,y])
                        elif q_data[white_previous[0],white_previous[1],white_previous[2],black_previous[0],black_previous[1],black_previous[2],piece,x,y]==best:
                            bests.append([piece,x,y])
                        """
                        if q_data[white_previous[0],white_previous[1],white_previous[2],black_previous[0],black_previous[1],black_previous[2],piece,x,y]>-99999:
                            bests.append([piece,x,y])
                        """
            best_index=choice(bests)
            reward=move(board,best_index[0],best_index[1],best_index[2])
            while reward==-1:
                bests.remove(best_index)
                if bests==[]:
                    print('miss')
                    break;
                q_data[white_previous[0],white_previous[1],white_previous[2],black_previous[0],black_previous[1],black_previous[2],best_index[0],best_index[1],best_index[2]]=q_data[white_previous[0],white_previous[1],white_previous[2],black_previous[0],black_previous[1],black_previous[2],best_index[0],best_index[1],best_index[2]]-99999
                best_index=choice(bests)
                reward=move(board,best_index[0],best_index[1],best_index[2])
                

            
            if reward==-1:
                q_data[white_previous[0],white_previous[1],white_previous[2],black_previous[0],black_previous[1],black_previous[2],best_index[0],best_index[1],best_index[2]]=q_data[white_previous[0],white_previous[1],white_previous[2],black_previous[0],black_previous[1],black_previous[2],best_index[0],best_index[1],best_index[2]]-99999
                gameover=1
            else:
                black.append([white_previous[0],white_previous[1],white_previous[2],black_previous[0],black_previous[1],black_previous[2],best_index[0],best_index[1],best_index[2]])
                if reward>=0:
                    point=point+1
                e=1
                for i in range(len(white)-1,-1,-1):
                    q_data[white[i][0],white[i][1],white[i][2],white[i][3],white[i][4],white[i][5],white[i][6],white[i][7],white[i][8]]=q_data[white[i][0],white[i][1],white[i][2],white[i][3],white[i][4],white[i][5],white[i][6],white[i][7],white[i][8]]-reward*e
                    e=e/10
                e=1
                for i in range(len(black)-1,-1,-1):
                    q_data[black[i][0],black[i][1],black[i][2],black[i][3],black[i][4],black[i][5],black[i][6],black[i][7],black[i][8]]=q_data[black[i][0],black[i][1],black[i][2],black[i][3],black[i][4],black[i][5],black[i][6],black[i][7],black[i][8]]+reward*e
                    e=e/10
                    
                if reward>=1000:
                    print("black win!")
                    gameover=1
                    #break;
                    
    if gameover==1 or point>100:
        
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




    
np.save("E:\chess_ai_data\\test2",q_data) 