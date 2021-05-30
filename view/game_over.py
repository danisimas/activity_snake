import sys
import time
import pygame


pygame.init()
window = pygame.display.set_mode((600, 600))
window_rect = window.get_rect()
pygame.display.set_caption("Snake")


def game_over():
    window.fill((144, 238, 144))
    font = pygame.font.Font("assets/Vermin Vibes 1989.ttf", 48)
    font_2 = pygame.font.Font("assets/Vermin Vibes 1989.ttf", 38)
    text_1 = 'GAME OVER'
    text_2 = "Press espace to back menu"
    text_1 = font.render(text_1, True, (0, 0, 0))
    text_2 = font_2.render(text_2, True, (0, 0, 0))
    window.blit(text_1, (175, 250))
    window.blit(text_2, (85, 350))




def back():
    pass



