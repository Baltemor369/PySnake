import pygame as py
import time
import random as rd

from const import *
from snake import Snake
from food import Food

py.init()

# Créer l'écran
screen = py.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
py.display.set_caption('Snake Game')

clock = py.time.Clock()
snake_size = 10
snake_speed = 15

# Définir la police
police_style = py.font.SysFont(None, 50)

def message(txt:str, color:tuple[int,int,int], offset:int):
    msg_surface = police_style.render(txt, True, color)
    msg_rect = msg_surface.get_rect(center=(WINDOW_WIDTH/2, 0+offset))
    screen.blit(msg_surface, msg_rect)

def game():
    game_close = False
    snake = Snake(WINDOW_WIDTH/2, WINDOW_HEIGHT/2)

    while not game_close:
        # Graphics
        screen.fill(BROWN)

        message("PySnake", WHITE, (WINDOW_WIDTH/4, WINDOW_HEIGHT/6))
        py.display.update()

        # Handle Events
        for event in py.event.get():
            if event.type == py.QUIT:
                game_close = True
            if event.type == py.KEYDOWN:
                if event.key == py.K_q:
                    game_close = True
                
        
        py.display.update()
        
        # Update Game
        

    clock.tick(snake_speed)

    py.quit()
    quit()

game()