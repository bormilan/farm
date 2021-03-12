import pygame
import game
import menu
import fajl_kezelesek
import textinput

#menü felülete
def mentes(gombok):  
    #szöveg
    font = pygame.font.SysFont('Arial', 42)
    black = pygame.Color('#000000')
    text = font.render('Üres', True, black)
    
    #ablak
    window = pygame.display.set_mode((800,800))
    pygame.display.set_caption('pipacs farm')
    pygame.display.set_icon(pygame.image.load('logo.png'))
    
    window.fill(pygame.Color('#000000'))
    
    #mentések
    window.blit(pygame.image.load('mentes.png'), (gombok[0].x,gombok[0].y -100))
    window.blit(pygame.image.load('mentes.png'), (gombok[1].x,gombok[1].y -100))
    window.blit(pygame.image.load('mentes.png'), (gombok[2].x,gombok[2].y -100))
    
    window.blit(pygame.image.load('mentes.png'), (gombok[6].x,gombok[6].y -100))

    #szöveg
    font = pygame.font.SysFont('Arial', 42)
    black = pygame.Color('#000000')
    white = pygame.Color('#FFFFFF')
    text = font.render('Válaszd ki hogy hova szeretnél menteni', True, white)
    text1 = font.render('1', True, black)
    text2 = font.render('2', True, black)
    text3 = font.render('3', True, black)
    text4 = font.render('nincs mentés',True,black)
    
    window.blit(text, (100, 0))
    window.blit(text1, (gombok[0].x + 220,gombok[0].y + 90 -100))
    window.blit(text2, (gombok[1].x + 220,gombok[1].y + 90 -100))
    window.blit(text3, (gombok[2].x + 220,gombok[2].y + 90 -100))
    window.blit(text4, (gombok[6].x + 120,gombok[6].y + 90 -100))
    
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
                    if x > gombok[i].x and x < (gombok[i].szel + gombok[i].x) and y > (gombok[i].y + 75 -100) and y < (gombok[i].mag + (gombok[i].y -100)):
                        return(i)
                    
        #kilépésgomb           
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = event.pos
                if x > gombok[6].x and x < (gombok[6].szel + gombok[6].x) and y > (gombok[6].y + 75 -100) and y < (gombok[6].mag + (gombok[6].y -100)):
                    menu.main()
                    
        #kilépés vége
        if event.type == pygame.QUIT:
            quit = True