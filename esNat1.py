from random import *

'''
1: Scrivi una funzione generatrice di password. La funzione deve generare 
una stringa alfanumerica di 8 caratteri qualora l'utente voglia una password semplice, 
o di 20 caratteri ascii qualora desideri una password più complicata.
'''
def es1():
    sem=1
    com=2
    alfanum=[range(49, 58), range (65, 91), range(97, 123)]
    #random.seed()
    dom=int(input("inserire 1 per passwod semplice o 2 per complessa:  "))
    pswrdL=[]
    if dom==sem:
        numCar=8
        while len(pswrdL)!=numCar:
            rRang=randint(0, (len(alfanum)-1))
            car=alfanum[rRang] [randrange(0, (len(alfanum[rRang])))]
            pswrdL.append(chr(car))
    elif dom==com:
        numCar=20
        while len(pswrdL)!=numCar:
            rRang=randint(0, (len(alfanum)-1))
            car=alfanum[rRang] [randrange(0, (len(alfanum[rRang])))]
            pswrdL.append(chr(car))
    else:
        pswrdL=["errore di input"]
    pswrd="".join(pswrdL)
    print(pswrd)






'''
Un indirizzo MAC (Media Access Control address) è un indirizzo univoco associato dal produttore, 
a una NIC, composto da 6 coppie di cifre esadecimali separate da due punti.
Un esempio di MAC è 02:FF:A5:F2:55:12.
Scrivi una funzione genera_mac che generi degli indirizzi MAC pseudo casuali.
'''
def es2():
    macList=[]
    num=6

    while len(macList)!=num:
        macList.append(hex(randint(0,255)))
    macAd=" : ".join(macList)
    print(macAd)


'''
3: Nella serie di Fibonacci, ciascun numero della serie è la somma dei due numeri nella serie che lo precedono, ad esempio:
1, 1, 2, 3, 5, 8, 13 (...)
Scrivi una funzione ricorsiva che restituisce in output i numeri della sequenza di Fibonacci, entro una soglia specifica impostata dall'utente.
'''
def fiboRicors(soglia, n1, n2):
    if n1==1 and n2==1:
            print(n1)
            print(n2)
    if soglia==0:
        return
    else:
        n=n1+n2
        print(n)
        fiboRicors(soglia-1, n2, n)

        
def es3():
    lst=[]
    num=0
    while num<1:
        num=int(input("inserire  soglia per fibonacci(minimo 1):  "))
    
    if num==1:
        print(num)
    else:
        fiboRicors(num-2, 1, 1)#1 e 1 sono i primi 2 numeri
'''
Il ROT-15 è un semplice cifrario monoalfabetico, in cui ogni lettera del messaggio da cifrare viene sostituita con quella posta 15 posizioni più avanti nell'alfabeto.
Scrivi una semplice funzione in grado di criptare una stringa passata, o decriptarla se la stringa è già stata precedentemente codificata.
'''

def cifro(frase):
    
    #letter=range(97, 123)
    risul=""
    for car in frase:
        risul=risul+chr((((ord(car)-97)+15)%26)+97)
    return risul

def decifro(frase):
    risul=""
    for car in frase[:-1]:
        numSost=(ord(car)-97)-15
        if numSost<0:
            numSost=26+(ord(car)-97)-15
            risul=risul+chr(numSost+97)
    risul=risul+chr(numSost+97)
    return risul 

def es4():
    
    scelta =0
    while int(scelta)<1 or int(scelta)>2:
        scelta=input("inserire 1 per criptare e 2 per decriptare:    ")
    frase=input("inserisci una stringa: ")
    if int(scelta)==1:
        ris=cifro(frase)
    else:
        ris=decifro(frase)
    print(ris)
'''
Il file annual.csv (allegato) contiene la anomalia della temperatura globale del pianeta Terra dal 1880 ad oggi, proveniente da varie fonti (colonna “Source”).
Scrivere un programma che generi un dizionario che abbia come chiave l’anno (“Year”) 
e valore la media aritmetica delle anomalie registrate dalle varie fonti durante quell’anno.
Inoltre scrivere una funzione che dati in input due anni diversi (anno_1 e anno_2) trovi la anomalia massima e minima nel periodo compreso tra anno_1 e anno_2.
'''
def trovaMaxeMinDaA(listaAnnual):
    anno_1=int(input("DA:   "))
    anno_2=int(input("A:   "))
    listaInteressata=[]

    if anno_1<=anno_2:
        for i in range(anno_1, (anno_2+1)):
            listaInteressata.append(float(listaAnnual[str(i)]))
        return max(listaInteressata), min(listaInteressata)
    else:
        print("ERRORE DI INPUT")
        return "error", "error"







def es6():
    ReadData = open("annual.csv", "r").readlines()
    listaAnnual={}
    cntRighe = 0   
    temp = 0.0    #variabile di appoggio
    media=0
    count=2
    for riga in ReadData[1:]:   #scorrimento file
        annoSucc=ReadData[count].split(",")
        letturaRiga = riga[:-1].split(",")  #lettura riga
        cntRighe+=1
        temp=temp+float(letturaRiga[2])
        if float(annoSucc[1])!=float(letturaRiga[1]):
            listaAnnual[letturaRiga[1]] = temp/cntRighe #dizionario{numero anno : media valori}
            temp=0
            cntRighe=1
        if count<len(ReadData)-1:
            count+=1
        else:
            count=1
        
    print(listaAnnual)
    massimo, minimo=trovaMaxeMinDaA(listaAnnual)
    print(massimo)
    print (minimo)
   


def main():
    es6()

if __name__ == "__main__":
	main()
