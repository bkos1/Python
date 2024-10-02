gyumolcsok=['alma', 'körte', 'barack', 'banán', 'eper', 'füge', 'dinnye']
print(gyumolcsok[0], gyumolcsok[2])
print(gyumolcsok[0:5])
print(gyumolcsok[-5:])
print(gyumolcsok[1:6])

#Csere

gyumolcsok[0]= 'áfonya'
print(gyumolcsok)

#Ciklus

for x in gyumolcsok:
    print(x, end= ' - ')
print()

for i in range(len(gyumolcsok) - 1):
    print(gyumolcsok[i], end= ' * ')
print(gyumolcsok[-1])

print()

gyumi = "citrom"
if gyumi in gyumolcsok:
    print(f'A(z) {gyumi} benne van a listában.')
else:
    print(f'A(z) {gyumi} nincs benne a listában.')
print()

gyumolcsok[1:3] = ['ananász', 'mangó', 'kiwi']
print(gyumolcsok)

gyumolcsok[-3:-1] = ['szilva']
print(gyumolcsok)

gyumolcsok.insert(1, 'licsi')
print( gyumolcsok)

gyumolcsok.append('szőlő')
print(gyumolcsok)

zöldségek = ['répa', 'retek', 'hagyma']

zöldségek.append('káposzta')
print(zöldségek)

gyumolcsok.extend(zöldségek)
print(gyumolcsok)

zöldségek[-2:] = []
print(zöldségek)

zöldségek.remove("retek")
print(zöldségek)

szamaim = [2, 4, 6, 8, 12]
szamaim.remove(4)
print(szamaim)

elem = szamaim.pop()
print(szamaim)
print(elem)

for o in range(len(gyumolcsok)):
    gyumolcsok[o] = gyumolcsok[o].capitalize()
print(gyumolcsok)
print()

összeg = 0
for y in gyumolcsok:
    összeg += len(y)
print(f'A lista elemeinek összes hossza: {összeg}')

for z in gyumolcsok:
    gyumolcsok.reverse()
print(gyumolcsok)


lst = list(range(0,10,2))
print(lst)

szamok = [12, 2, 50, 30, 89, 11, 3, 67, 88, 75, 25, 2, 25, 25, 50, 3 ]
#szamok.sort()
#szamok.sort(reverse=True)
#szamok.reverse()
szamok.sort(key=lambda x: abs(25 - x)) #rakd sorrendbe a számokat a 25-től való távolságuk alapján
print(szamok)

gyumolcsok.sort()
print(gyumolcsok)

nevek = ['Alma', 'bimbo', 'cica', 'Dávid', 'Eperke', 'frici']
#nevek.sort()
#nevek.sort(key=lambda x: x.lower())
nevek.sort(key=str.lower)
print(nevek)

lst1 = [1, 2, 3, 4, 5,]
# lst2 = lst1.copy()
# lst2 = lst1[:]
lst2 = list(lst1)
print(lst2, lst1)
lst1.append(9)
print(lst2, lst1)

print(szamok.count(3))
print(szamok.count(25))
print(nevek.count('Eperke'))

print(szamok.index(3))
print(nevek.index('Eperke'))

txt = 'Képzeld, nyertem a lottón, ... kettesem volt.'
szavak = txt.split()
# szavak = txt.split('.')
# szavak = list(txt)
print(szavak)