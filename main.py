import pygame
import sys
import playerClass

pygame.init()

background = pygame.image.load("GameBoardTemp.jpg")
player = pygame.image.load("PlayerTemp.jpg")

screen = pygame.display.set_mode((800, 600))
screen.blit(background, (0, 0))
pygame.display.update()
while 1:
    for event in pygame.event.get():
        if event.type in (pygame.QUIT, pygame.KEYDOWN):
            sys.exit()



