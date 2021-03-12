import pygame
import pygame.gfxdraw
 
def nev_be():
    hibas = False

    window = pygame.display.set_mode((480, 200))
    pygame.display.set_caption('mentési név megadása')
    
    clip = window.get_clip()
    x = 40
    y = 80
    width = 400
    height = 40
    destination = pygame.Rect(x, y, width, height)
    window.set_clip(destination)
    
    white = pygame.Color('#FFFFFF')
    black = pygame.Color('#000000')
    font = pygame.font.SysFont('Arial', 32)
 
    user_input = ''
    enter = False
    quit = False
    while (not quit) and (not enter):
        #szöveg kiírása
        text = font.render(user_input + '', True, black)
        # szöveg kirajzolása
        pygame.gfxdraw.box(window, destination, white)
        pygame.gfxdraw.rectangle(window, destination, white)
        text = font.render(user_input + '', True, black)
        window.blit(text, destination)
        pygame.display.update()
 
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                enter = True
            elif event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]
            else:
                user_input += event.unicode
 
        for i in range(len(user_input)):
            if user_input[i] in 'abcdefghijklmnopqrstuvwxyz':
                pass
            else:
                user_input = nev_be()
                quit = True
 
        if event.type == pygame.QUIT:
            pygame.event.post(event)
            quit = True
            
 
    window.set_clip(clip);
    return user_input