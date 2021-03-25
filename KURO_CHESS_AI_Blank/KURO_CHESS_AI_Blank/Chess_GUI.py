import pygame
from chess_engine import*
import numpy as np
from random import*
import time
q_data=np.load("test1.npy")
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
gameover=0
while not done:
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
    reward=move(board,best_index[0],best_index[1],best_index[2])
    while reward ==-1:
        best_index=choice(bests)
        reward=move(board,best_index[0],best_index[1],best_index[2])
    white.append([field_index[0],field_index[1],field_index[2],field_index[3],best_index[0],best_index[1],best_index[2]])
    if reward>=1000:
        print("white win!")
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
        reward=move(board,best_index[0],best_index[1],best_index[2])
        while reward ==-1:
            best_index=choice(bests)
            reward=move(board,best_index[0],best_index[1],best_index[2])
        black.append([field_index[0],field_index[1],field_index[2],field_index[3],best_index[0],best_index[1],best_index[2]])
        if reward>=1000:
            print("black win!")
            gameover=1
    for event in pygame.event.get():# User did something
        if event.type == pygame.QUIT:# If user clicked close
            done=True # Flag that we are done so we exit this loop
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
        print(white)
        print(black)
    time.sleep(1)
pygame.quit()