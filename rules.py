import pygame
import menu

#szabályok gomb felülete
def rules(gombok):
    #ablak
    window = pygame.display.set_mode((800,800))
    pygame.display.set_caption('pipacs farm')
    pygame.display.set_icon(pygame.image.load('logo.png'))
    
    window.fill(pygame.Color('#000000'))
    
    #kép beszúrása
    window.blit(pygame.image.load('szabalyok2.png'),(10,0))
    
    #vissza gomb
    window.blit(pygame.image.load('back.png'), (0,0))
    
    pygame.display.update()
    
         #kilépés eleje
    quit = False
    while not quit:
        pygame.init()
        event = pygame.event.wait()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = event.pos
                if x > gombok[3].x and x < gombok[3].szel and y > gombok[3].y and y < gombok[3].mag:
                    menu.main()
        
        #kilépés vége
        if event.type == pygame.QUIT:
            quit = True