import pygame
import sys
from pygame.math import Vector2
import random

class SNAKE :
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(6,10),Vector2(7,10)]
        self.direction = Vector2(1,0)
    def draw_snake(self):
        for block in self.body:
            #create and draw the blocks
            X_pos = int(cell_size*block.x)
            Y_pos = int(cell_size*block.y)
            block_rect = pygame.Rect(X_pos,Y_pos,cell_size,cell_size)
            pygame.draw.rect(screen,(255,0,0),block_rect)

    def move_snake(self):
        updated_body = self.body[:-1]
        updated_body.insert(0,updated_body[0]+self.direction)
        



class FRUIT :
    def __init__(self):
        #create x and y position
        self.x = random.randint(0,cell_number-1)
        self.y = random.randint(0,cell_number-1)
        self.pos = Vector2(self.x,self.y) #Using vectors is easier than using list

    def draw_fruit(self):
        #create and draw a rectangle
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size)
        pygame.draw.rect(screen,(126,166,114),fruit_rect)

pygame.init()
cell_size = 30
cell_number = 20
fruit = FRUIT()
snake = SNAKE()
screen = pygame.display.set_mode((cell_number*cell_size,cell_number*cell_size)) #initialise game window
clock = pygame.time.Clock()
while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            pygame.quit()
            sys.exit()
    screen.fill((175,215,70))
    fruit.draw_fruit()
    snake.draw_snake()
    pygame.display.update()
    clock.tick(60) #executes the loop at 60FPS





