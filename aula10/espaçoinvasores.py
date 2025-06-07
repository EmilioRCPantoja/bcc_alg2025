import pygame
import pyautogui



pygame.init()

larguratela, alturatela = pyautogui.size()

janela = pygame.display.set_mode((larguratela, alturatela-100 ))


x = 20
y = 400

yplayer = alturatela - 160
xplayer = 40

xbullet=xplayer+25
ybullet = yplayer-20

xinimigo = larguratela - 1320

sentido=1

inim = [
    pygame.Rect(xinimigo,40,70,55), pygame.Rect(xinimigo + 130, 40, 70, 55),
    pygame.Rect(xinimigo + 250, 40, 70, 55), pygame.Rect(xinimigo + 370, 40, 70, 55 ),
    pygame.Rect(xinimigo + 490, 40, 70, 55), pygame.Rect(xinimigo + 610, 40, 70, 55)]


sentido = 1

clock = pygame.time.Clock()

bala=False


rodar = True
while rodar:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodar = False

    cor = ("#ffffff")

    pk = pygame.key.get_pressed()

    if pk[pygame.K_d]:
        xplayer += 2
    if pk[pygame.K_a]:
        xplayer -= 2
    if pk[pygame.K_w] and not bala:
        xbullet = xplayer + 25
        ybullet = yplayer - 20
        bala = True

    



    janela.fill(("#000000"))
    #player
    pygame.draw.rect(janela, cor, (xplayer, yplayer, 17, 25) )
    pygame.draw.rect(janela, cor, (xplayer+17, yplayer-20, 20, 30) )
    pygame.draw.rect(janela, cor, (xplayer+37, yplayer, 17, 25) )

    for i in range(len(inim)):
        pygame.draw.rect(janela, "#FFFFFF", inim[i])

    if bala:
        pygame.draw.circle(janela, ("#ffffff"),[xbullet, ybullet], 15, 5 )
        ybullet -= 3
        if ybullet<0:
            bala = False

    pygame.display.flip()

    ybullet -= 3*sentido

    clock.tick(120)