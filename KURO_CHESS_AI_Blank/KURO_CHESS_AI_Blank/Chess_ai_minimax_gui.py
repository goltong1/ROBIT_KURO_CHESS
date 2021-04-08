
import pygame
from chess_engine import*
import numpy as np
from random import*
import time
import copy
def random_piece_move(board,piece):
    cases=[]
    now=find(board,abs(piece))
    for x in range(0,8):
        for y in range(0,8):
            if check(board,piece,now[0],now[1],x,y):
                cases.append([piece,x,y])
    return choice(cases)
def find_best_move(board,turn,n):
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
        if turn and reward>=6:
            return case
        elif not(turn) and reward>10:
            return case
        if n<3:
            next_best=find_best_move(tmp_board,not(turn),n+1)
            reward=reward-move(tmp_board,next_best[0],next_best[1],next_best[2])
        if reward>best:
            best_index=case
            best=reward
            bests=[]
            bests.append(case)
        elif reward==best:
            bests.append(case)
    if best==0:
        best_index=choice(bests)
    if n==1:
        print(best)
    return best_index
SCREEN_WIDTH=800
SCREEN_HEIGHT=800
pygame.init()
SCREEN=pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
BLACK= ( 90,  90,  90)
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
turn=True
clicked=False
now_x=0
now_y=0
move_x=0
move_y=0
white_previous=[16,0,0]
black_previous=[16,0,0]
gameover=0
count=0
previous=[]
castling_w=[1,1,1]
opening=False
my_face=False
print('white Turn')
while not done:
    if turn:
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
                    previous=[abs(board[int(now_y)][int(now_x)]),int(move_x),int(move_y)]
                    reward=move(board,abs(board[int(now_y)][int(now_x)]),int(move_x),int(move_y))
                    if reward!=-1:
                        if board[move_y][move_x]==28:
                            castling_w[0]=0
                        elif board[move_y][move_x]==24:
                            castling_w[1]=0
                        elif board[move_y][move_x]==31:
                            castling_w[2]=0
                        turn=False
                        print('black Turn')
                    else:
                        if (board[now_y][now_x]==28 and castling_w[0]) and ((board[move_y][move_x]==24 and castling_w[1]) or (board[move_y][move_x]==31 and castling_w[2])):
                            if castling(board,board[now_y][now_x],board[move_y][move_x]):
                                castling_pieces=[board[now_y][now_x],board[move_y][move_x]]
                                turn=False
                                if castling_pieces[0]==28:
                                    castling_w[0]=0
                                if castling_pieces[1]==24:
                                    castling_w[1]=0
                                elif castling_pieces[1]==31:
                                    castling_w[2]=0
                                turn=False
                                print('black Turn')
                            else:
                                print("wrong position!")
                    clicked=False
                    
    else:
        if turn!=True:
            if reward>=1000:
                print("white win!")
                gameover=1
            else:
                if count==0:
                    if previous==[20,4,4]:
                        best=[12,4,3]
                        opening=True
                    elif previous==[19,3,4]:
                        best=[11,3,3]
                        opening=True
                    elif previous[0]==25 or previous[0]==30:
                        knight=choice([1,6])
                        best=random_piece_move(board,knight)
                    else:
                        best=[12,4,3]
                        my_face=True
                elif count<2:
                    if opening:
                        if previous[0]==25 or previous[0]==30:
                            knight=choice([1,6])
                            best=random_piece_move(board,knight)
                    elif my_face:
                        best=[11,3,2]
                    else:
                        best=find_best_move(board,turn,3)
                else:
                    best=find_best_move(board,turn,1)
                reward=move(board,best[0],best[1],best[2])
                count=count+1
                if reward>=1000:
                    print('black win!')
                    gameover=1
                turn=True;
                print('white Turn')

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
    