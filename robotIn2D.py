# pavimento RETTANGOLARE diviso in piastrelle
# alcune piastrelle sono "rosse" ovvero con ostacoli
# piastrelle "verdi" è dove sta il robot
# (lista di liste=matrice)
# calcolare il percorso più breve per arrivare da A a B 
# movim solo sopra sotto destra sinistra
# risultato:{0:[1,5], 1(-->dalla cella) :[0,6,2](-->posso andare in)}
#
#
# 0 = libero
# -1 = ostacolo




import pygame
import sys



pavimento=[[0, 0, 0, -1, -1], [-1, 0, 0, 0, -1], [0, 0, -1, -1, -1], [0, 0, -1, 0, 0], [-1, 0, 0, 0, 0], [-1, -1, -1, 0, 0]]
dimensione=50
XGR=len(pavimento[0])*dimensione
YGR=len(pavimento)*dimensione
#RGB
NERO=(0, 0, 0)
BIANCO=(255, 255, 255)
ROSSO=(255, 0, 0)


def drawgrid():
    
    for x in range (0, XGR, dimensione):
        for y in range (0, YGR, dimensione):
            piastrella=pygame.Rect(x, y, dimensione, dimensione)
            pygame.draw.rect(screen, BIANCO, piastrella, 1)
            if pavimento[int(y/dimensione)][int(x/dimensione)]==-1:
                ostacolo=pygame.Rect(x, y, dimensione, dimensione)  
                pygame.draw.rect(screen, ROSSO, ostacolo) 
    





def numerazion():
    global pavimento
    numer=0
    for n in range(0, len(pavimento)):
        for i in range(0, len(pavimento[n])):
            if pavimento[n][i]!=-1:
                pavimento[n][i]=numer
                numer=numer+1

def creaDiz():
    #lista=[[0,1], [0,-1], [-1,0], [1,0]]
    global pavimento
    dizio={}
    listaPoss=[]
    for n in range(0, len(pavimento)):
        for i in range(0, len(pavimento[n])):
            if pavimento[n][i]!=-1:
                if n!=0:
                    if pavimento[n-1][i]!=-1:
                        listaPoss.append(pavimento[n-1][i])
                if i!=0:
                    if pavimento[n][i-1]!=-1:
                        listaPoss.append(pavimento[n][i-1])   
                if i!=(len(pavimento[n])-1):
                    if pavimento[n][i+1]!=-1:
                        listaPoss.append(pavimento[n][i+1])
                if n!=(len(pavimento)-1):
                    if pavimento[n+1][i]!=-1:
                        listaPoss.append(pavimento[n+1][i])
                dizio[pavimento[n][i]]=listaPoss
                listaPoss=[]
            

def main():
    #print(f"righe:{len(pavimento)} colonne: {len(pavimento[0])}")
    numerazion()
    creaDiz()
    #----------SCREEN----------
    global screen
    pygame.init()
    screen= pygame.display.set_mode((XGR, YGR))
    screen.fill(NERO)
    while True:
        drawgrid()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
    

if __name__ == "__main__":
	main()