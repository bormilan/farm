import pygame
import menu
import time
import mentes
import load
import fajl_kezelesek
import sys
import textinput

#földek classa
class Foldek:
    def __init__(self,index,x,y):
        self.index = index
        self.x = x
        self.y = y
        self.allapot = 0
        self.tipus = ""
        self.ido = 0

#toolbar classa, minden "kattintható gomb"-nak külön adatai vannak
class toolbar:
    def __init__(self,x,y,szel,mag):
        self.x = x
        self.y = y
        self.szel = szel
        self.mag = mag

def menu_mentes(befold,foldek,penz,i,j,foldeksz,gombok):
    foldek_m = []
    for l in range(befold):
        foldek_m.append(foldek[j][l])
    hanyadik = mentes.mentes(gombok)
    fajl_kezelesek.kiiras(hanyadik,befold,penz,foldek_m,textinput.nev_be(),hanyadik,foldeksz)
    menu.main()
    
def novekedes(befold,tipusok,foldek,novesiidok,window,foldkepek,viragok,kinottek,i,j):
    tipus_sz = 0
    for i in range(befold):
        for k in range(len(tipusok)):
            if tipusok[k] == foldek[j][i].tipus:
                tipus_sz = k
        if foldek[j][i].ido + novesiidok[tipus_sz] <= round(time.time())  :
            if foldek[j][i].allapot == 1:
                window.blit(foldkepek.image, (foldek[j][i].x,foldek[j][i].y), pygame.Rect(foldkepek.ures,foldkepek.SIZE))
                foldek[j][i].allapot = 0
            elif foldek[j][i].allapot == 2:
                for k in range(len(viragok)):
                    if foldek[j][i].tipus == tipusok[k]:
                        window.blit(foldkepek.image, (foldek[j][i].x,foldek[j][i].y), pygame.Rect(kinottek[k+3],foldkepek.SIZE))
                foldek[j][i].allapot = 3
    pygame.time.set_timer(pygame.USEREVENT, 1)

def ultetes(window,foldkepek,foldek,tipusok,viragok,i,j,k):
    window.blit(foldkepek.image, (foldek[j][i].x,foldek[j][i].y), pygame.Rect(foldkepek.vetett,foldkepek.SIZE))
    foldek[j][i].allapot = 1
    foldek[j][i].tipus = tipusok[k]
    viragok[k] = False
    #nullázás hogy tényleg a megfelelő idő teljen el
    foldek[j][i].ido = round(time.time())
    
def ontozes(window,foldkepek,foldek,i,j):
    window.blit(foldkepek.image, (foldek[j][i].x,foldek[j][i].y), pygame.Rect(foldkepek.ontozott,foldkepek.SIZE))
    foldek[j][i].allapot = 2

def foldek_betolt(filesz,befold,foldek,j):
    if filesz != 0:
        for i in range(befold):
            foldek[j][i].allapot = int(fajl_kezelesek.beolvas(filesz-1)[i+2].split(" ")[0])
            foldek[j][i].tipus = fajl_kezelesek.beolvas(filesz-1)[i+2].split(" ")[1]
            foldek[j][i].ido = int(fajl_kezelesek.beolvas(filesz-1)[i+2].split(" ")[2])
    else:
        for i in range(befold):
            foldek[j][i].allapot = 0
            foldek[j][i].tipus = ""
            foldek[j][i].ido = 0
            
def fold_kepek_megjelenit(befold,foldek,foldkepek,kinottek,viragok,j,window,tipusok):
    for i in range(befold):
        for k in range(3):
            if foldek[j][i].allapot == k:
                window.blit(foldkepek.image, (foldek[j][i].x,foldek[j][i].y), pygame.Rect(kinottek[k],foldkepek.SIZE))
        if foldek[j][i].allapot == 3:
            for k in range(len(viragok)):
                if foldek[j][i].tipus == tipusok[k]:
                    window.blit(foldkepek.image, (foldek[j][i].x,foldek[j][i].y), pygame.Rect(kinottek[k+3],foldkepek.SIZE))
                    
def arak_kiirasa(veteli_arak,window,toolbarok):
    font = pygame.font.SysFont('Arial', 42)
    black = pygame.Color('#000000')
    for i in range(len(veteli_arak)):
        text = font.render("{:>3}$".format(veteli_arak[i]),True,black)
        window.blit(text, (toolbarok[3].x - 80,toolbarok[3].y + 20 +(i*100)))
        
def aratas(window,foldkepek,foldek,viragok,tipusok,penz,eladasi_arak,i,j,gombok):
    font = pygame.font.SysFont('Arial', 32)
    black = pygame.Color('#000000')
    window.blit(foldkepek.image, (foldek[j][i].x,foldek[j][i].y), pygame.Rect(foldkepek.ures,foldkepek.SIZE))
    for k in range(len(viragok)):
        if foldek[j][i].tipus == tipusok[k]:
            penz += eladasi_arak[k]
            window.blit(pygame.image.load('pont.png'), (gombok[5].x,gombok[5].y))
    text = font.render(str(int(penz)), True, black)
    window.blit(text, (gombok[5].x + 80,gombok[5].y+30))
    foldek[j][i].allapot = 0
    foldek[j][i].tipus = ""
    return penz

def mod_kivalasztas(modok,window,i):
    modok = [False] *3
    modok[i] = True
    window.blit(pygame.image.load('hatter04.jpg'),(460,810),pygame.Rect((460,810),(320,100)))
    return modok

def virag_modok(penz,veteli_arak,modok,window,viragok,i,gombok):
    font = pygame.font.SysFont('Arial', 32)
    black = pygame.Color('#000000')
    red = pygame.Color('#ff0000')
    
    window.blit(pygame.image.load('hatter04.jpg'),(460,810),pygame.Rect((460,810),(320,100)))
    viragok[i] = True
    window.blit(pygame.image.load('pont.png'), (gombok[5].x,gombok[5].y))
    text = font.render(str(int(penz)), True, black)
    window.blit(text, (gombok[5].x + 80,gombok[5].y+30))
    
    return viragok

def nincspenz(penz,veteli_arak,modok,window,viragok,i,gombok):
    font = pygame.font.SysFont('Arial', 32)
    black = pygame.Color('#000000')
    red = pygame.Color('#ff0000')
    window.blit(pygame.image.load('hatter04.jpg'),(460,840),pygame.Rect((460,840),(250,100)))
    text_elso_sor = font.render("nincs elég pénzed,", True, red)
    text_masodik_sor = font.render("vagy nem vagy jó módban!", True, red)
    window.blit(text_elso_sor, (460,810))
    window.blit(text_masodik_sor, (460,840))

def kikapalas(window,foldkepek,foldek,i,j):
    window.blit(foldkepek.image, (foldek[j][i].x,foldek[j][i].y), pygame.Rect(foldkepek.ures,foldkepek.SIZE))
    foldek[j][i].allapot = 0
    foldek[j][i].ido = 0
    
def penz_kiir(window,penz):
    window.blit(pygame.image.load('pont.png'), (800,0))
    
    font = pygame.font.SysFont('Arial', 32)
    black = pygame.Color('#000000')
    text = font.render(str(int(penz)), True, black)
    window.blit(text, (880,30))

def jatek(befold,filesz):
    gombok = [menu.Gombok(150,100,480,150),menu.Gombok(150,300,480,150),menu.Gombok(150,500,480,150),menu.Gombok(0,0,100,100),menu.Gombok(780,800,200,100),menu.Gombok(800,0,100,100),menu.Gombok(150,700,480,150)]
    foldeksz = [4,8,16]
    toolbarok = [toolbar(0,780,100,200),toolbar(100,780,100,200),toolbar(200,780,100,200),toolbar(900,120,100,100),toolbar(900,220,100,100),toolbar(900,320,100,100),toolbar(900,420,100,100),toolbar(900,520,100,100),toolbar(900,620,100,100),toolbar(900,720,100,100)]
    veteli_arak= [5,10,25,50,100]
    eladasi_arak = [10,20,50,100,200]
    
    kepek = [menu.Kepek('hatter04.jpg',0,0),menu.Kepek('toolbar02.png',toolbarok[0].x,toolbarok[0].y),menu.Kepek('viragoktoolbar.png',toolbarok[3].x,toolbarok[3].y),menu.Kepek('pont.png',800,0),menu.Kepek('exit.png',gombok[4].x,gombok[4].y)]
    
    #mennyi idő alatt nőjjön ki a növény
    tipusok = ["piros","sarga","kek","fekete","rozsaszin"]
    novesiidok = [10,20,30,60,360]

    #hivatkozás létrehozása
    foldkepek = menu.FoldKepek()
    
    pygame.time.set_timer(pygame.USEREVENT, 1)
    
    #földek
    foldek = [[Foldek(0,10,10),Foldek(1,200,10),Foldek(2,10,200),Foldek(3,200,200)],
              [Foldek(0,10,10),Foldek(1,200,10),Foldek(2,400,10),Foldek(3,600,10),Foldek(4,10,200),Foldek(5,200,200),Foldek(6,400,200),Foldek(7,600,200)],
              [Foldek(0,10,10),Foldek(1,200,10),Foldek(2,400,10),Foldek(3,600,10),Foldek(4,10,200),Foldek(5,200,200),Foldek(6,400,200),Foldek(7,600,200),Foldek(8,10,400),Foldek(9,200,400),Foldek(10,400,400),Foldek(11,600,400),Foldek(12,10,600),Foldek(13,200,600),Foldek(14,400,600),Foldek(15,600,600)]]
     
     #bool változók, hogy mi van kijelölve
        #alsó toolbar
    modok = [False,False,False]
            #magok,ontozes,vetes
    
        #oldalsó toolbar
    viragok = [False,False,False,False,False]
                #piros,sárga,kék,fekete,rózsaszín
    
    #földek számának megállapítása
    if befold == 0:
        befold = int(fajl_kezelesek.beolvas(filesz-1)[0])
    
    #megnézi hogy hány földünk van
    j = 0
    for k in range(3):
            if foldeksz[k] == befold:
                j = k                # j = hanyadik a foldeksz nevű listában
    
    #földek adatainak a megfelelő mentés szerinti beállítása
    foldek_betolt(filesz,befold,foldek,j)
    
    #ablak
    window = pygame.display.set_mode((1000,900))
    pygame.display.set_caption('pipacs farm')
    pygame.display.set_icon(pygame.image.load('logo.png'))
    
    #képek berakása
        #háttér
    bg = window.blit(pygame.image.load(kepek[0].nev), (kepek[0].x,kepek[0].y))
    
    #kinőtt virágok képei
    kinottek = [foldkepek.ures,foldkepek.vetett,foldkepek.ontozott,foldkepek.kinottpiros,foldkepek.kinottsarga,foldkepek.kinottkek,foldkepek.kinottfekete,foldkepek.kinottrozsaszin]
    
            #képek berakása
    for i in range(5):
        window.blit(pygame.image.load(kepek[i].nev),(kepek[i].x,kepek[i].y))
    
        #földek megjelenítése
    fold_kepek_megjelenit(befold,foldek,foldkepek,kinottek,viragok,j,window,tipusok)
                    
    #árak kiírása
    arak_kiirasa(veteli_arak,window,toolbarok)
    
    #pénz gyűjtése
    if filesz == 0:
        penz = 5
    else:
        penz = int(fajl_kezelesek.beolvas(filesz-1)[1])
    
    pygame.display.update()
    
    #kilépés eleje
    quit = False
    while not quit:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            quit = True
        
        for k in range(3):
            if foldeksz[k] == befold:
                j = k
        
        #folyamatosan ki legyen írva a helyes összege a játékosnak
        penz_kiir(window,penz)
              
        #menügomb
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = event.pos
                if x > gombok[4].x and x < (gombok[4].szel + gombok[4].x)  and y > gombok[4].y and y < (gombok[4].mag + gombok[4].y):
                    menu_mentes(befold,foldek,penz,i,j,foldeksz,gombok)
        
        #növekedés
        if event.type == pygame.USEREVENT:
            novekedes(befold,tipusok,foldek,novesiidok,window,foldkepek,viragok,kinottek,i,j) 
    
    #főprogramrész
        pygame.init()
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if event.button == 1:
                x, y = event.pos
                for i in range(befold):
                    if x < (foldek[j][i].x + 175) and x > foldek[j][i].x and y > foldek[j][i].y and y < (foldek[j][i].y +175):
                        #ültetés
                        if foldek[j][i].allapot == 0 and modok[0]:
                            for k in range(len(viragok)):
                                if viragok[k]:
                                    ultetes(window,foldkepek,foldek,tipusok,viragok,i,j,k)
                        #öntözés   
                        elif foldek[j][i].allapot == 1 and modok[1]:
                            ontozes(window,foldkepek,foldek,i,j)  
                        #aratás
                        elif foldek[j][i].allapot == 3 and modok[2]:
                            penz += aratas(window,foldkepek,foldek,viragok,tipusok,penz,eladasi_arak,i,j,gombok)
                             
                            
                #alsó toolbar-on a jelenlegi mód kiválasztása 
                for i in range(3):
                    if x > toolbarok[i].x and x < (toolbarok[i].x + toolbarok[i].szel) and y > toolbarok[i].y and y  < (toolbarok[i].y + toolbarok[i].mag):
                        modok = mod_kivalasztas(modok,window,i)
                
                #az oldalsó toolbar-on a virág kiválasztása
                for i in range(len(viragok)):
                    if x > toolbarok[i+3].x and x < (toolbarok[i+3].x + toolbarok[i+3].szel) and y > toolbarok[i+3].y and y < (toolbarok[i+3].y + toolbarok[i+3].mag):
                        if veteli_arak[i] <= penz:
                            viragok = virag_modok(penz,veteli_arak,modok,window,viragok,i,gombok)
                            penz -= veteli_arak[i]
                        else:
                            nincspenz(penz,veteli_arak,modok,window,viragok,i,gombok)
   
        #kikapálás(minden esetben üressé teszi a földet)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                x, y = event.pos
                for i in range(befold):
                    if x < (foldek[j][i].x + 175) and x > foldek[j][i].x and y > foldek[j][i].y and y < (foldek[j][i].y + 175):
                        kikapalas(window,foldkepek,foldek,i,j)
                        
        pygame.display.update()          
    sys.exit()