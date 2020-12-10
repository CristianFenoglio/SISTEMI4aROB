def playrandom(playlist):
    for i,elemento 


file=open("./music.csv","r")
playlist=[]
for riga in file:
    #print(riga, end=" ")#l'end permette di modificare la messa a capo automatica
                        #evita infatti che vad<a a capo in automatico e puoi mettere un carattere qualsiasi
    a=riga[0:-1].split(",")
    appoggio={"numero":a[0], "nome":a[1], "author":a[2]}
    playlist.append(appoggio)

    
print(playlist)

playrandom(playlist)



file.close()
