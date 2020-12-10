import pygame
import sys

if __name__ =="__main__":
    pygame.init()

    screen = pygame.display.set_mode((650,650)) #initialise game window
    clock = pygame.time.Clock()
    # test_surface = pygame.Surface((200,200))
    # test_surface.fill((121, 216, 224))
    # test_rect = test_surface.get_rect(center = (325,325))
    #display_surface.fill((152, 235, 52)) #Lime green background
    #Define a event loop
    while True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                pygame.quit()
                sys.exit()
        screen.fill((175,215,70))
        # screen.blit(test_surface,test_rect) #blit-> block image transfer
        pygame.display.update()
        clock.tick(60) #executes the loop at 60FPS





