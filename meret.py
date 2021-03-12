import pygame
import menu
import game

# a pálya méretének kiválasztása
def meret_kivalaszt(gombok,foldeksz):
    #ablak
    window = pygame.display.set_mode((800,800))
    pygame.display.set_caption('pipacs farm')
    pygame.display.set_icon(pygame.image.load('logo.png'))
    
    window.fill(pygame.Color('#000000'))
    
    #szöveg
    font = pygame.font.SysFont('Arial', 42)
    black = pygame.Color('#000000')
    text1 = font.render('2x2', True, black)
    text2 = font.render('2x4', True, black)
    text3 = font.render('4x4', True, black)
    
    #2x2
    window.blit(pygame.image.load('mentes.png'), (gombok[0].x,gombok[0].y)) 
    #2x4
    window.blit(pygame.image.load('mentes.png'), (gombok[1].x,gombok[1].y))
    #4x4
    window.blit(pygame.image.load('mentes.png'), (gombok[2].x,gombok[2].y))
    
    #söveg kiírása
    window.blit(text1, (350,190))
    window.blit(text2, (350,390))
    window.blit(text3, (350,590))
        
    pygame.display.update()
    
        #kilépés eleje
    quit = False
    while not quit:
        pygame.init()
        event = pygame.event.wait()
        
        #gombok
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = event.pos
                for i in range(3):
                    if x > gombok[i].x and x < (gombok[i].szel + gombok[i].x) and y > (gombok[i].y + 75) and y < (gombok[i].mag + gombok[i].y):
                        return (foldeksz[i])
    
    #kilépés vége
        if event.type == pygame.QUIT:
            quit = True