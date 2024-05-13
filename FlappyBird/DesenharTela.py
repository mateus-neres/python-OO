import pygame
import os

TELA_LARGURA = 500
TELA_ALTURA = 800
pygame.font.init()
FONTE_PONTOS = pygame.font.SysFont("arial", 50)
IMAGEM_FUNDO = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bg.png")))

def DesenharTela(tela, passaros, canos, chao, pontos): 
    tela.blit(IMAGEM_FUNDO, (0, 0))  

    for passaro in passaros:
        passaro.desenhar(tela)

    for cano in canos:
        cano.desenhar(tela)

    chao.desenhar(tela)

    pontos_texto = FONTE_PONTOS.render(f"Pontos: {pontos}", 1, (255, 255, 255))
    tela.blit(pontos_texto, (TELA_LARGURA - pontos_texto.get_width() - 10, 10)) 

    pygame.display.update()