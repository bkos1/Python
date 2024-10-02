#1. feladat
szamok1 = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
szamok2 = list(range(2,21))
print(szamok2)
print()
#2. feladat
txt="The end justifies the means"
szöveg=txt.split()
print(szöveg)
print()
#3. feladat
for i in range(len(szöveg)):
    szöveg[i] = szöveg[i].capitalize()
print(szöveg)
print()

lst = [0,1]
for i in range(8):
    lst.append(lst[-2]+lst[-1])
print(lst)
