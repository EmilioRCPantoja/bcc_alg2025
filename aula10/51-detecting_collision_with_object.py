# referência:
# https://stackoverflow.com/questions/29640685/how-do-i-detect-collision-in-pygame

import pygame

pygame.init()

# tamanho da janela
window = pygame.display.set_mode((1200, 750))

# desenha o retângulo que vai perceber a colisão
rect = pygame.Rect(300, 200, 80, 150)

# posição inicial de uma bola na tela
x = 25
y = 300

# sentido para o qual a bola caminha
sentido = 1

# pega a referência temporal para poder fazer espera mais à frente
clock = pygame.time.Clock()

run = True
while run:

    # código obrigatório para finalizar bem o programa
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # obtém a posição do círculo em forma de ponto
    if sentido >=0 :
        point = (x, y)

    else:
        point = (x-20, y)
    # verifica se houve colisão do 
    # ponto (centro do círculo) com o retângulo
    collide = rect.collidepoint(point)

    # coloca uma cor ou outra, dependendo se houve ou não colisão
    # esse é um if arretado inline potentão
    # você consegue converter esse if para o formato normal?
    # essa é uma boa questão de prova :-)
    color = (255, 0, 0) if collide else (255, 255, 255)

    # desenha informações na tela
    window.fill("purple")    
    pygame.draw.rect(window, color, rect) # desenho do retângulo
    pygame.draw.circle(window, (10, 10, 10), [x, y], 15, 5) # desenho do círculo
    pygame.display.flip()

    # o circulo (centro) vazou a borda da janela?
    if x > 1180 or x < 20:
       sentido *= -1 # inverte o sentido 

    # varia a posição do círculo
    x += 3 * sentido

    # espera um pouco
    clock.tick(60) 

pygame.quit()
