import pygame
import menu
import game
import fajl_kezelesek

#load game felülete
def load(gombok):    
    #szöveg
    font = pygame.font.SysFont('Arial', 42)
    black = pygame.Color('#000000')
    white = pygame.Color('#FFFFFF')
    text = font.render('Üres', True, black)
    text1 = font.render('Mentések',True,white)
    
    #ablak
    window = pygame.display.set_mode((800,800))
    pygame.display.set_caption('pipacs farm')
    pygame.display.set_icon(pygame.image.load('logo.png'))
    
    window.fill(pygame.Color('#000000'))
    
    #mentések
    window.blit(pygame.image.load('mentes.png'), (gombok[0].x,gombok[0].y))
    window.blit(pygame.image.load('mentes.png'), (gombok[1].x,gombok[1].y))
    window.blit(pygame.image.load('mentes.png'), (gombok[2].x,gombok[2].y))
    
    #feliratok a gombokra
    window.blit(text1, (300, 0))
        #elso gomb felirata
    for i in range(3):
        if fajl_kezelesek.betoltes()[i] == 1:
            text21 = font.render(str(fajl_kezelesek.nev_beolvas(i)), True, black)
            window.blit(text21, (gombok[i].x + 190,gombok[i].y + 90))
        else:
            window.blit(text, (gombok[i].x + 190,gombok[i].y + 90))
        
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
                    
        #gombok
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = event.pos
                for i in range(3):
                    if x > gombok[i].x and x < (gombok[i].szel + gombok[i].x) and y > (gombok[i].y + 75) and y < (gombok[i].mag + gombok[i].y):
                        if fajl_kezelesek.betoltes()[i] == 1:
                            return (i + 1)
                    
        #kilépés vége
        if event.type == pygame.QUIT:
            quit = True