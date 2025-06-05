import pygame
import pyautogui


pygame.init()

largtela, altela = pyautogui.size()

janela = pygame.display.set_mode((largtela, altela))


x = 20
y = 400

yr = 900
xr = 40

inim = [pygame.Rect(20,40,100,55), pygame.Rect(150, 40, 100, 55), pygame.Rect(280, 40, 100,  55)]


sentido = 1

clock = pygame.time.Clock()


rodar = True
while rodar:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodar = False

    ponto = (x, y)

    cor = ("#ffffff")

    pk = pygame.key.get_pressed()

    if pk[pygame.K_d]:
        xr += 1
    if pk[pygame.K_a]:
        xr -= 1


    janela.fill((45,65,68))
    
    pygame.draw.rect(janela, cor, (xr, yr, 50, 50) )
    for i in range(len(inim)):
        pygame.draw.rect(janela, "#000000", inim[i])

    pygame.display.flip()

    clock.tick(120)