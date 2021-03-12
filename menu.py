import pygame
import pygame.gfxdraw
import meret
import load
import rules
import game

#menü
def main():
    pygame.init()
    foldeksz = [4,8,16]
    gombok = [Gombok(150,100,480,150),Gombok(150,300,480,150),Gombok(150,500,480,150),Gombok(0,0,100,100),Gombok(780,800,200,100),Gombok(800,0,100,100),Gombok(150,700,480,150)]
    
    #színek
    white = pygame.Color('#FFFFFF')
    szurke = pygame.Color('#817D96')

    #ablak
    window = pygame.display.set_mode((800,800))
    pygame.display.set_caption('pipacs farm')
    pygame.display.set_icon(pygame.image.load('logo.png'))
    
    window.fill(pygame.Color('#000000'))
    
    font = pygame.font.SysFont('Bauhaus 93', 60)
    text = font.render('Pipacsfarm', True, white)
    window.blit(text, (240, 0))
    
    font = pygame.font.SysFont('Courier New', 20)
    text = font.render('Készítette: Bór Milán    P6G6KI', True, white)
    window.blit(text, (428, 780))
    
        #gombok
    kepek = ['newgame.png','loadgame.png','szabalyok.png']
    for i in range(3):
        window.blit(pygame.image.load(kepek[i]), (gombok[i].x,gombok[i].y))
    
    pygame.display.update()
    
    #modulok változói hogy a gombokat ciklusba lehessen rakni
    modulok = [meret.meret_kivalaszt,load.load,rules.rules]
    
        #kilépés eleje
    quit = False
    while not quit:
        pygame.init()
        event = pygame.event.wait()
        
        #gombok
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = event.pos
                if x > gombok[0].x and x < (gombok[0].szel + gombok[0].x) and y > (gombok[0].y + 75) and y < (gombok[0].mag + gombok[0].y):
                    game.jatek(modulok[0](gombok,foldeksz),0)
                    
                if x > gombok[1].x and x < (gombok[1].szel + gombok[1].x) and y > (gombok[1].y + 75) and y < (gombok[1].mag + gombok[1].y):
                        game.jatek(0,modulok[1](gombok))
                        
                if x > gombok[2].x and x < (gombok[2].szel + gombok[2].x) and y > (gombok[2].y + 75) and y < (gombok[2].mag + gombok[2].y):
                        modulok[2](gombok)
                    
        #kilépés vége
        if event.type == pygame.QUIT:
            quit = True
            
    pygame.quit()
        
#gombok classa
class Gombok:
    def __init__(self,x,y,szelesseg,magassag):
        self.x = x
        self.y = y
        self.szel = szelesseg
        self.mag = magassag

#képek pozícióinak classa
class FoldKepek:
    def __init__(self):
        self.SIZE = (155,155)
        
        self.ures = (10,10)
        self.vetett = (185,10)
        self.ontozott = (10,185)
        self.kinottpiros = (185,185)
        self.kinottsarga = (370,10)
        self.kinottkek = (370,185)
        self.kinottfekete = (540,10)
        self.kinottrozsaszin = (540,185)
        
        self.image = pygame.image.load('pipacsok.png')
        
class Kepek:
    def __init__(self,nev,x,y):
        self.nev = nev
        self.x = x
        self.y = y
        
if __name__ == '__main__':
    main()
