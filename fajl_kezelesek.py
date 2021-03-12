import pygame
import game

#file beolvasása, változók aszerinti betöltése
def beolvas(filesz):
    szavak = []
    fajlnevek = [("mentes1.txt"),("mentes2.txt"),("mentes3.txt")]
    
    for i in range(3):
        if filesz == i:
            with open(fajlnevek[i],"r") as f:
                while True:
                    sor = f.readline()
                    sor = sor.rstrip("\n")
                    if sor == "":
                        return szavak
                    else:
                        szavak.append(sor)

#fájlba kiírása a játék adatainak
def kiiras(mentsz,befold,penz,foldek_m,nev,ertek,foldeksz):
    fajlnevek = [("mentes1.txt"),("mentes2.txt"),("mentes3.txt")]
    
    #megnézi hogy hány földünk van
    for k in range(3):
        if foldeksz[k] == befold:
            j = k
    
    #nevek beolvasása
    with open("nevek.txt","r",encoding="utf-8") as f:
        nevek = []
        for i in range(3):
            sor = f.readline()
            sor = sor.rstrip("\n")
            nevek.append(sor)
            
    #slotok megváltoztatása
    szavak = []
    with open("slotok.txt","r",encoding="utf-8")as f:
        for i in range(3):
            sor = f.readline()
            sor = sor.rstrip("\n")
            szavak.append(int(sor))
      
    szavak[ertek] = 1
    with open("slotok.txt","w",encoding="utf-8") as f:    
        for i in range(3):
            f.write("{}\n".format(szavak[i]))
    
    #adatok kiírása
    for i in range(3):
        if mentsz == i:
            with open(fajlnevek[i],"w") as f:
                f.write("{}\n".format(befold))
                f.write("{}\n".format(penz))
                for j in range(befold):
                    f.write("{} {} {}\n".format(foldek_m[j].allapot,foldek_m[j].tipus,foldek_m[j].ido))
                    
                with open("nevek.txt","w") as f:
                    nevek[i] = nev
                    for j in range(3):
                        f.write("{}\n".format(nevek[j]))
                
def betoltes():
    szavak = []
    
    with open("slotok.txt","r",encoding="utf-8")as f:
        for i in range(3):
            sor = f.readline()
            sor = sor.rstrip("\n")
            szavak.append(int(sor))
        
    return szavak  
            
def nev_beolvas(ertek):
    with open("nevek.txt","r",encoding="utf-8") as f:
        for i in range(3):
            sor = f.readline()
            sor = sor.rstrip("\n")
            if i == ertek:
                return sor