szam1 = int(input("Adj meg egy számot: "))
szam2 = int(input("Adj meg egy számot: "))
játékos1 = szam1 % 3
játékos2 = szam2 % 3
            
#kő= 0
#papír= 1
#olló = 2
if játékos1 == játékos2:
    print ("Döntetlen")
elif játékos1 == 0 and játékos2 == 2:
     print("Játékos 1 nyert.")
elif  játékos1 == 1 and játékos2 == 0:
     print("Játékos 1 nyert.")
elif  játékos1 == 2 and játékos2 == 1:
    print ("Játékos 1 nyert.")
else:
    print ("Játékos 2 nyert.")