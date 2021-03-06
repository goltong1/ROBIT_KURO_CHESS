
import pygame
from chess_engine import*
import numpy as np
from random import*
import time
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
gameover=0
now_x=0
now_y=0
move_x=0
move_y=0
castling_w=[1,1,1]
castling_b=[1,1,1]

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
                if reward!=-1:
                    turn=False
                    if board[move_y][move_x]==28:
                        castling_w[0]=0
                    elif board[move_y][move_x]==24:
                        castling_w[1]=0
                    elif board[move_y][move_x]==31:
                        castling_w[2]=0
                else:
                    if (board[now_y][now_x]==28 and castling_w[0]) and ((board[move_y][move_x]==24 and castling_w[1]) or (board[move_y][move_x]==31 and castling_w[2])):
                        castling_pieces=[board[now_y][now_x],board[move_y][move_x]]
                        if castling(board,board[now_y][now_x],board[move_y][move_x]):
                            turn=False
                            if castling_pieces[0]==28:
                                castling_w[0]=0
                            if castling_pieces[1]==24:
                                castling_w[1]=0
                            elif castling_pieces[1]==31:
                                castling_w[2]=0
                        else:
                            print("wrong position!")
                    else:
                        print("wrong position!")
                clicked=False
            elif turn==False and not(clicked):
                now_x = event.pos[0]//100
                now_y = event.pos[1]//100
                if piece_exist(board,now_x,now_y)>=0 and piece_exist(board,now_x,now_y)<16:
                    clicked=True
            elif turn==False and clicked:
                move_x = event.pos[0]//100
                move_y = event.pos[1]//100
                reward=move(board,abs(board[int(now_y)][int(now_x)]),int(move_x),int(move_y))
                if reward!=-1:
                    turn=True
                    if board[move_y][move_x]==4:
                        castling_b[0]=0
                    elif board[move_y][move_x]==0:
                        castling_b[1]=0
                    elif board[move_y][move_x]==7:
                        castling_b[2]=0
                else:
                    if (board[now_y][now_x]==4 and castling_b[0]) and ((board[move_y][move_x]==0 and castling_b[1]) or (board[move_y][move_x]==7 and castling_b[2])):
                        castling_pieces=[board[now_y][now_x],board[move_y][move_x]]
                        if castling(board,board[now_y][now_x],board[move_y][move_x]):
                            turn=True
                            if castling_pieces[0]==4:
                                castling_b[0]=0
                            if castling_pieces[1]==0:
                                castling_b[1]=0
                            elif castling_pieces[1]==71:
                                castling_b[2]=0
                        else:
                            print("wrong position!")

                    else:
                        print("wrong position!")
                clicked=False

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

