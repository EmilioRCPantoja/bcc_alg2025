
#copia descarada de espace invaders, apenas não consegui implementar a colisão
#por falta de tempo, mas pretendo continuar o projeto depois das provas :D

import pygame
import pyautogui
#inicia pyautogui
pygame.init()

#identfica o tamanho da tela do monitor atual
larguratela, alturatela = pyautogui.size()

#define o tamanho da janela do jogo com base na tela do monitor atual
janela = pygame.display.set_mode((larguratela, alturatela-100 ))

#define a posição inicial do player
yplayer = alturatela - 160
xplayer = 40

#define a posição inicial da bala
xbullet= xplayer+25
ybullet = yplayer-20

#define o eixo x do inimigo
xinimigo = larguratela - 1320

#define o sentido da bala
sentido=1

#define a posição dos inimigos
inim = [
    pygame.Rect(xinimigo,40,70,55), pygame.Rect(xinimigo + 130, 40, 70, 55),
    pygame.Rect(xinimigo + 250, 40, 70, 55), pygame.Rect(xinimigo + 370, 40, 70, 55 ),
    pygame.Rect(xinimigo + 490, 40, 70, 55), pygame.Rect(xinimigo + 610, 40, 70, 55)]

#identifica a referência temporal
clock = pygame.time.Clock()

#estado inicial da bala
bala=False


rodar = True
while rodar:

    #codigo para finalizar o programa
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodar = False


    cor = ("#ffffff")

    #identifica a tecla pressionada pelo usuário
    pk = pygame.key.get_pressed()
    #movimentaçãõ do player no eixo x
    if pk[pygame.K_d]:
        xplayer += 2
    if pk[pygame.K_a]:
        xplayer -= 2
    #define as posições iniciais e dispara a bala
    if pk[pygame.K_w] and not bala:
        xbullet = xplayer + 25
        ybullet = yplayer - 20
        bala = True

    #preenche a janela
    janela.fill(("#000000"))
    
    #desenha o player
    pygame.draw.rect(janela,("#ffffff"), (xplayer, yplayer, 17, 25) )
    pygame.draw.rect(janela, ("#ffffff"), (xplayer+17, yplayer-20, 20, 30) )
    pygame.draw.rect(janela, ("#ffffff"), (xplayer+37, yplayer, 17, 25) )

    #desenha os inimigos
    for i in range(len(inim)):
        pygame.draw.rect(janela, cor , inim[i])

    #desenha a bala continuamente a partir de quando é disparada
    if bala:
        pygame.draw.circle(janela, ("#ffffff"),[xbullet, ybullet], 15, 5 )
        ybullet -= 3
        if ybullet<0:
            bala = False

    pygame.display.flip()

    #varia a posição da bala
    ybullet -= 2*sentido

    clock.tick(120)