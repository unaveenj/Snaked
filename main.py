import pygame
import sys
from pygame.math import Vector2
import random

class SNAKE :
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(2,10)]
        self.direction = Vector2(1,0)
        self.create_block = False
    def draw_snake(self):
        for block in self.body:
            #create and draw the blocks
            X_pos = int(cell_size*block.x)
            Y_pos = int(cell_size*block.y)
            block_rect = pygame.Rect(X_pos,Y_pos,cell_size,cell_size)
            pygame.draw.rect(screen,(255,0,0),block_rect)

    def move_snake(self):
        if self.create_block == True:
            updated_body = self.body[:]
            updated_body.insert(0,updated_body[0]+self.direction)
            self.body = updated_body[:] #update the original body
            self.create_block = False
        else:
            updated_body = self.body[:-1]
            updated_body.insert(0,updated_body[0]+self.direction)
            self.body = updated_body[:] #update the original body


    def add_block(self):
        self.create_block = True




class FRUIT :
    def __init__(self):
        self.fruit_placer()


    def draw_fruit(self):
        #create and draw a rectangle
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size)
        pygame.draw.rect(screen,(126,166,114),fruit_rect)

    def fruit_placer(self):
        #create x and y position
        self.x = random.randint(0,cell_number-1)
        self.y = random.randint(0,cell_number-1)
        self.pos = Vector2(self.x,self.y) #Using vectors is easier than using list


class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()

    def update(self):
        self.snake.move_snake()
        self.collision()
        self.check_fail()


    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()

    def collision(self): #checks is snake ate the apple
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.fruit_placer()
            self.snake.add_block()

            # print("EATEN !!!") #test print statement
    def check_fail(self):
        #check if snake outside the boundary
        if not 0<=self.snake.body[0].x<cell_number or not 0<=self.snake.body[0].y<cell_number :
            self.game_over()

        #check if snake hits itslef
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()



    def game_over(self):
        pygame.quit()
        sys.exit()


pygame.init()
cell_size = 30
cell_number = 20

screen = pygame.display.set_mode((cell_number*cell_size,cell_number*cell_size)) #initialise game window
clock = pygame.time.Clock()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

main_game = MAIN()

while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN: #event conditions for arrows keys
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y !=1:
                    main_game.snake.direction = Vector2(0,-1) #Move the snake up
            elif event.key == pygame.K_LEFT:
                if main_game.snake.direction.x !=1:
                    main_game.snake.direction = Vector2(-1,0)
            elif event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x !=-1:
                    main_game.snake.direction = Vector2(1,0)
            elif event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0,1)
    screen.fill((175,215,70))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60) #executes the loop at 60FPS




