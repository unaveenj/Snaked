import pygame
import sys
from pygame.math import Vector2
import random
from pygame.image import load

class SNAKE :
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(2,10)]
        self.direction = Vector2(1,0)
        self.create_block = False

        #Head
        self.head_up = load("resources/head_up.png")
        self.head_down = load("resources/head_down.png")
        self.head_left = load("resources/head_left.png")
        self.head_right = load("resources/head_right.png")
        self.head = self.head_right
        #Tail
        self.tail_up = load("resources/tail_up.png")
        self.tail_down = load("resources/tail_down.png")
        self.tail_left = load("resources/tail_left.png")
        self.tail_right = load("resources/tail_right.png")
        self.tail = self.tail_right

        #body
        self.body_vertical = load("resources/body_vertical.png")
        self.body_horizontal = load("resources/body_horizontal.png")

        #turning
        self.body_tl = load("resources/body_tl.png")
        self.body_tr = load("resources/body_tr.png")
        self.body_br = load("resources/body_br.png")
        self.body_bl = load("resources/body_bl.png")

        #sound
        self.collision_sound = pygame.mixer.Sound('resources/ding.mp3')
        self.bang_sound= pygame.mixer.Sound('resources/crash.mp3')
        # self.bgm = pygame.mixer.music.load('resources/my_bgm.mp3')





    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()
        for index,block in enumerate(self.body):
            X_pos = int(cell_size*block.x)
            Y_pos = int(cell_size*block.y)
            block_rect = pygame.Rect(X_pos,Y_pos,cell_size,cell_size)
            
            #draw head
            if index == 0 :
                screen.blit(self.head,block_rect)
            elif index == len(self.body)-1:
                screen.blit(self.tail,block_rect)
            else:
                prev_block = self.body[index+1] - block
                next_block = self.body[index -1] - block
                if prev_block.x == next_block.x:
                    screen.blit(self.body_vertical,block_rect)
                elif prev_block.y == next_block.y:
                    screen.blit(self.body_horizontal,block_rect)
                else:
                    if prev_block.x==-1 and next_block.y==-1 or prev_block.y==-1 and next_block.x==-1:
                        screen.blit(self.body_tl,block_rect)
                    elif prev_block.x == -1 and next_block.y == 1 or prev_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl, block_rect)
                    elif prev_block.x==1 and next_block.y==-1 or prev_block.y==-1 and next_block.x==1:
                        screen.blit(self.body_tr,block_rect)
                    elif prev_block.x == 1 and next_block.y == 1 or prev_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br, block_rect)

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

    def update_head_graphics(self):
        head_relation_vector = self.body[1] - self.body[0]
        if head_relation_vector == Vector2(1,0): self.head = self.head_left
        elif head_relation_vector == Vector2(-1,0): self.head = self.head_right
        elif head_relation_vector == Vector2(0,1): self.head = self.head_up
        elif head_relation_vector == Vector2(0,-1): self.head = self.head_down


    def update_tail_graphics(self):
        tail_relation_vector = self.body[-2] - self.body[-1]
        if tail_relation_vector == Vector2(1,0): self.tail = self.tail_left
        elif tail_relation_vector == Vector2(-1,0): self.tail = self.tail_right
        elif tail_relation_vector == Vector2(0,1): self.tail = self.tail_up
        elif tail_relation_vector == Vector2(0,-1): self.tail = self.tail_down

    def add_block(self):
        self.create_block = True


    def play_collision_sound(self):
        self.collision_sound.play()

    def play_crash_sound(self):
        self.bang_sound.play()





class FRUIT :
    def __init__(self):
        self.fruit_placer()


    def draw_fruit(self):
        #create and draw a rectangle
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size)
        screen.blit(apple,fruit_rect)
        # pygame.draw.rect(screen,(126,166,114),fruit_rect)

    def fruit_placer(self):
        #create x and y position
        self.x = random.randint(0,cell_number-1)
        self.y = random.randint(0,cell_number-1)
        self.pos = Vector2(self.x,self.y) #Using vectors is easier than using list


class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
        # self.snake.play_bgm()

    def update(self):
        self.snake.move_snake()
        self.collision()
        self.check_fail()


    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()

    def collision(self): #checks is snake ate the apple
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.fruit_placer()
            self.snake.add_block()
            self.snake.play_collision_sound()

        for block in self.snake.body[1:]:
            if block==self.fruit.pos:
                self.fruit.fruit_placer()


            # print("EATEN !!!") #test print statement
    def check_fail(self):
        #check if snake outside the boundary
        if not 0<=self.snake.body[0].x<cell_number or not 0<=self.snake.body[0].y<cell_number :
            self.snake.play_crash_sound()
            self.game_over()

        #check if snake hits itslef
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()



    def game_over(self):
        pygame.quit()
        sys.exit()

    def draw_score(self):
        score_text = str(len(self.snake.body)-3)
        score_surface = game_font.render(score_text,True,(56,74,4))
        pos_x = int(cell_size*cell_number-50)
        pos_y = int(cell_size*cell_number-50)
        score_rect = score_surface.get_rect(center=(pos_x,pos_y))
        apple_rect = apple.get_rect(midright = (score_rect.left,score_rect.centery))


        screen.blit(score_surface,score_rect)
        screen.blit(apple,apple_rect)




pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()

cell_size = 30
cell_number = 20

screen = pygame.display.set_mode((cell_number*cell_size,cell_number*cell_size)) #initialise game window
clock = pygame.time.Clock()
#Graphics
apple = pygame.image.load('resources/apple.png').convert_alpha()
game_font = pygame.font.Font("PoetsenOne.ttf",25)

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




