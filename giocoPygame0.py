import pygame
import sys

ALTEZZA=600
LARGHEZZA=600
#RGB
NERO=(0, 0, 0)
BIANCO=(255, 255, 255)
ROSSO=(255, 0, 0)
def drawgrid():
    dimensione=50
    for x in range (0, LARGHEZZA, dimensione):
        for y in range (0, ALTEZZA, dimensione):
            piastrella=pygame.Rect(x, y, dimensione, dimensione)
            pygame.draw.rect(screen, BIANCO, piastrella, 1)
    ostacolo=pygame.Rect(50, 100, dimensione, dimensione)  
    pygame.draw.rect(screen, ROSSO, ostacolo) 

def main():
    global screen
    pygame.init()
    screen= pygame.display.set_mode((ALTEZZA, LARGHEZZA))
    screen.fill(NERO)
    while True:
        drawgrid()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()




if __name__=="__main__":
    main()