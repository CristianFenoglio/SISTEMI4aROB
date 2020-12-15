import random
def playrandom(playlist):
    random.seed()
    lisControl=[]
    while len(lisControl)!=len(playlist):
        num=random.randrange(len(playlist))
        if(not(num in lisControl)):
            print(playlist[num])
            lisControl.append(num)


        

def main():
    file=open("./music.csv","r")
    playlist=[]
    for riga in file:
        #print(riga, end=" ")#l'end permette di modificare la messa a capo automatica
                            #evita infatti che vada a capo in automatico e puoi mettere un carattere qualsiasi
        pezzoR=riga[0:-1].split(",")
        appoggio={"numero":pezzoR[0], "nome":pezzoR[1], "author":pezzoR[2]}
        playlist.append(appoggio)
    #print(playlist)
    playrandom(playlist)
    #playran4  dom(playlist)
    file.close()


if __name__ == "__main__":
	main()
