import pygame
from chess_engine import*
import numpy as np
from random import*
import time

q_data=np.load("E:\chess_ai_data\\test2.npy")
SCREEN_WIDTH=800
SCREEN_HEIGHT=800
pygame.init()
SCREEN=pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
BLACK= ( 50,  50,  50)
WHITE= (255,255,255)
BLUE = ( 0,  0,255)
GREEN= ( 0,255,  0)
RED  = (255,  0,  0)
pygame.display.set_caption("CHESS_Blank")

clock = pygame.time.Clock()

 
pawnW = pygame.image.load("image\pawn_W.png")
pawnW= pygame.transform.scale(pawnW, (100, 100))
pawnB = pygame.image.load("image\pawn_B.png")
pawnB= pygame.transform.scale(pawnB, (100, 100))
bishopB = pygame.image.load("image\\bishop_B.png")
bishopB= pygame.transform.scale(bishopB, (100, 100))
bishopW = pygame.image.load("image\\bishop_W.png")
bishopW= pygame.transform.scale(bishopW, (100, 100))
kingW = pygame.image.load("image\\king_W.png")
kingW= pygame.transform.scale(kingW, (100, 100))
kingB = pygame.image.load("image\\king_B.png")
kingB= pygame.transform.scale(kingB, (100, 100))
knightB = pygame.image.load("image\\knight_B.png")
knightB= pygame.transform.scale(knightB, (100, 100))
knightW = pygame.image.load("image\\knight_W.png")
knightW= pygame.transform.scale(knightW, (100, 100))
queenW = pygame.image.load("image\\queen_W.png")
queenW= pygame.transform.scale(queenW, (100, 100))
queenB = pygame.image.load("image\\queen_B.png")
queenB= pygame.transform.scale(queenB, (100, 100))
rookB = pygame.image.load("image\\rook_B.png")
rookB= pygame.transform.scale(rookB, (100, 100))
rookW = pygame.image.load("image\\rook_W.png")
rookW= pygame.transform.scale(rookW, (100, 100))
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
white=[]
black=[]
turn=True
clicked=False
now_x=0
now_y=0
move_x=0
move_y=0
white_previous=[16,0,0]
black_previous=[16,0,0]
gameover=0
while not done:
    for event in pygame.event.get():# User did something
        if event.type == pygame.QUIT:# If user clicked close
            done=True # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if turn and not(clicked):
                now_x = event.pos[0]//100
                now_y = event.pos[1]//100
                if piece_exist(board,now_x,now_y)>15 and piece_exist(board,now_x,now_y)<32:
                    clicked=True
            elif turn and clicked:
                move_x = event.pos[0]//100
                move_y = event.pos[1]//100
                reward=move(board,abs(board[int(now_y)][int(now_x)]),int(move_x),int(move_y))
                if white!=[]:
                    white_previous=[white[len(white)-1][6]-16,white[len(white)-1][7],white[len(white)-1][8]]
                if black!=[]:
                    black_previous=[black[len(black)-1][6],black[len(black)-1][7],black[len(black)-1][8]]
                if reward!=-1:
                    turn=False
                    e=1
                    for i in range(len(black)-1,-1,-1):
                        q_data[black[i][0],black[i][1],black[i][2],black[i][3],black[i][4],black[i][5],black[i][6],black[i][7],black[i][8]]=q_data[black[i][0],black[i][1],black[i][2],black[i][3],black[i][4],black[i][5],black[i][6],black[i][7],black[i][8]]-reward*e
                        e=e/10
                    white.append([white_previous[0],white_previous[1],white_previous[2],black_previous[0],black_previous[1],black_previous[2],abs(board[int(now_y)][int(now_x)]),int(move_x),int(move_y)])
                else:
                    print("wrong position!")
                clicked=False
    if turn!=True:
        if reward>=1000:
            print("white win!")
            gameover=1
        else:
            if white!=[]:
                white_previous=[white[len(white)-1][6]-16,white[len(white)-1][7],white[len(white)-1][8]]
            if black!=[]:
                black_previous=[black[len(black)-1][6],black[len(black)-1][7],black[len(black)-1][8]]
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
                            best=[white_previous[0],white_previous[1],white_previous[2],black_previous[0],black_previous[1],black_previous[2],piece,x,y]
                            bests=[]
                            bests.append([piece,x,y])
                        elif q_data[white_previous[0],white_previous[1],white_previous[2],black_previous[0],black_previous[1],black_previous[2],piece,x,y]==best:
                            bests.append([piece,x,y])
            best_index=choice(bests)
            reward=move(board,best_index[0],best_index[1],best_index[2])
            while reward ==-1:
                bests.remove(best_index)
                if bests==[]:
                    print("random")
                    for piece in range(0,16):
                        if piece==0:
                            bests=[]
                        for x in range(0,8):
                            if find(board,piece)[0]==-1:
                                break;
                            for y in range(0,8):
                                if q_data[white_previous[0],white_previous[1],white_previous[2],black_previous[0],black_previous[1],black_previous[2],piece,x,y]>-9999:
                                    bests.append([piece,x,y])
                    while reward==-1:
                        best_index=choice(bests)
                        reward=move(board,best_index[0],best_index[1],best_index[2])
                    break;
                q_data[white_previous[0],white_previous[1],white_previous[2],black_previous[0],black_previous[1],black_previous[2],best_index[0],best_index[1],best_index[2]]=q_data[white_previous[0],white_previous[1],white_previous[2],black_previous[0],black_previous[1],black_previous[2],best_index[0],best_index[1],best_index[2]]-99999
                best_index=choice(bests)
                reward=move(board,best_index[0],best_index[1],best_index[2])
            black.append([white_previous[0],white_previous[1],white_previous[2],black_previous[0],black_previous[1],black_previous[2],best_index[0],best_index[1],best_index[2]])
            e=1
            for i in range(len(black)-1,-1,-1):
                q_data[black[i][0],black[i][1],black[i][2],black[i][3],black[i][4],black[i][5],black[i][6],black[i][7],black[i][8]]=q_data[black[i][0],black[i][1],black[i][2],black[i][3],black[i][4],black[i][5],black[i][6],black[i][7],black[i][8]]+reward*e
                e=e/10
            if reward>=1000:
                print("black win!")
                gameover=1    
            turn=True;

    SCREEN.fill(WHITE)
    for x in range(0,8):
        for y in range(0,8):
            if (x+y)%2==0:
                pygame.draw.rect(SCREEN, BLACK, [100*x,100*y,100,100])
            else:
                pygame.draw.rect(SCREEN, WHITE, [100*x,100*y,100,100])

    


    for y in range(0,8):
        for x in range(0,8):
            if abs(board[y][x])>7 and abs(board[y][x])<=15:
                if board[y][x]>=0:
                    SCREEN.blit(pawnB, [ x*100, y*100 ] )
                else:
                    SCREEN.blit(queenB, [ x*100, y*100 ] )
            elif abs(board[y][x])>15 and abs(board[y][x])<24:
                if board[y][x]>=0:
                    SCREEN.blit(pawnW, [ x*100, y*100 ] )
                else:
                    SCREEN.blit(queenW, [ x*100, y*100 ] )
            elif board[y][x]==1 or board[y][x]==6:
                SCREEN.blit(knightB, [ x*100, y*100 ] )
            elif board[y][x]==25 or board[y][x]==30:
                SCREEN.blit(knightW, [ x*100, y*100 ] )
            elif board[y][x]==2 or board[y][x]==5:
                SCREEN.blit(bishopB, [ x*100, y*100 ] )
            elif board[y][x]==26 or board[y][x]==29:
                SCREEN.blit(bishopW, [ x*100, y*100 ] )
            elif board[y][x]==0 or board[y][x]==7:
                SCREEN.blit(rookB, [ x*100, y*100 ] )
            elif board[y][x]==24 or board[y][x]==31:
                SCREEN.blit(rookW, [ x*100, y*100 ] )
            elif board[y][x]==3:
                SCREEN.blit(queenB, [ x*100, y*100 ] )
            elif board[y][x]==27:
                SCREEN.blit(queenW, [ x*100, y*100 ] )
            elif board[y][x]==4:
                SCREEN.blit(kingB, [ x*100, y*100 ] )
            elif board[y][x]==28:
                SCREEN.blit(kingW, [ x*100, y*100 ] )
                
    pygame.display.flip()

    #clock.tick(60)
    if gameover==1:
        done=True
        break;

    time.sleep(1)
pygame.quit()
    
np.save("test1",q_data) 

