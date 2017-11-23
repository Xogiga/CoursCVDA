import random

tab = []
maxi = 0
rng = 0 ##Commentaire au pif

def init():
    affichage = "."
    for i in range (0, maxi):
        for j in range (0, maxi):
            proba = random.randint(1,10)
            tab.append((proba,i,j,affichage))
    return tab

def affiche():
    for i in range (0, maxi):
        if i == 0:
            print (" ",i, end=" ")
        elif i == maxi-1:
            print (i)
        elif (i != 0 and i != maxi):
            print (i, end=" ")
            
    for i in range (0, maxi):
        print (i, end=" ")
        for j in range (0, maxi):
            print (tab[i+j*maxi][3], end =" ")
        print (" ")


def reveal():
    for i in range (0, maxi):
        if i == 0:
            print (" ",i, end=" ")
        elif i == maxi-1:
            print (i)
        elif (i != 0 and i != maxi):
            print (i, end=" ")
            
    for i in range (0, maxi):
        print (i, end=" ")
        for j in range (0, maxi):
            if tab[i+j*maxi][0] <= rng:
                if tab[i+j*maxi][3] != "x":
                    print("x", end=" ")
                else:
                    print(tab[i+j*maxi][3], end=" ")
            else :
                print (tab[i+j*maxi][3], end =" ")
        print (" ")

def choisir():
    x = -1
    y = -1
    while (x < 0 or y < 0 or x >= maxi or y >= maxi):
        print("Quel ligne ?")
        x=input("Ligne = ")
        print ("Quel collone ?")
        y = input("Collone = ")
        y=int(y)
        x=int(x)
        if (x < 0 or y < 0 or x >= maxi or y >= maxi):
            print("Pas dans la matrice")

    
    mine  = tab[x+y*maxi][0]
    if mine <= rng :
        tab[x+y*maxi] = (tab[x+y*maxi][0],x,y,"x")
        print ("PERDU")
        reveal()
        return False
    else :
        tab[x+y*maxi] = (tab[x+y*maxi][0],x,y,count(x,y))
        affiche()
        return True

def count(x,y):
    count = 0
    for i in range (x-1,x+2,1):
        for j in range (y-1,y+2,1):
            if (i+j*maxi) <= maxi*maxi-1:
                if (tab[i+j*maxi][0] <= rng):
                    count = count +1
    return count

def main():
    global tab
    global rng
    global maxi
    jouer = "o"
    while rng<1 or rng>=10:
        print("Quel probabilité (sur 10)?", end=" ")
        rng=int(input())
    while maxi<3 or maxi>10:
        print("Quel taille (entre 3 et 10)?", end=" ")
        maxi=int(input())
    while jouer == "o": 
        init()
        affiche()
        res = choisir()
        while res != False:
            res = choisir()
        print("Rejouer ? (O ou N)")
        jouer=input()
        tab = []
    
        

main()

    
