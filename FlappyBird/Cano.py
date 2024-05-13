import pygame
import os
import random

IMAGEM_CANO = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "pipe.png")))

class Cano:
    DISTANCIA = 200
    VELOCIDADE = 5

    def __init__(self, x):
        self.x = x
        self.altura = 0
        self.posicao_topo = 0
        self.posicao_base = 0
        self.CANO_BASE = IMAGEM_CANO
        self.CANO_TOPO = pygame.transform.flip(IMAGEM_CANO, False, True)
        self.passou = False
        self.definir_altura()

    def definir_altura(self):
        self.altura = random.randrange(50, 450)
        self.posicao_topo = self.altura - self.CANO_TOPO.get_height()
        self.posicao_base = self.altura + self.DISTANCIA

    def mover(self):
        self.x -= self.VELOCIDADE

    def desenhar(self, tela):
        tela.blit(self.CANO_TOPO, (self.x, self.posicao_topo))  
        tela.blit(self.CANO_BASE, (self.x, self.posicao_base))

    def colidir(self, passaro):
        passaro_mask = passaro.get_mask()
        topo_mask = pygame.mask.from_surface(self.CANO_TOPO)
        base_mask = pygame.mask.from_surface(self.CANO_BASE)

        distancia_topo = (self.x - passaro.x, self.posicao_topo - round(passaro.y))
        distancia_base = (self.x - passaro.x, self.posicao_base - round(passaro.y))

        base_ponto = passaro_mask.overlap(base_mask, distancia_base)
        top_ponto = passaro_mask.overlap(topo_mask, distancia_topo)

        if base_ponto or top_ponto:
            return True
        else:
            return False
