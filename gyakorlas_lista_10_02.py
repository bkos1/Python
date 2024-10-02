erdemjegy = [1,2,3,4,5]
osztaly = ['9/ny', '9/a', '10/b', '11/c', '12/b haladó']
adatok = ['Ákos', 'Dénes', 'Laci', 'Levente', 'Neli', 'Regi']

erdemjegy[0] = erdemjegy[2]
osztaly[1] = osztaly[2]
# adatok[-1] = adatok[2]
adatok[len(adatok)-1]=adatok[2]

print(erdemjegy)
print(adatok)
print(osztaly)
print()

print(len(erdemjegy))
for x in erdemjegy:
    print(x, end = ' ')
print()

del erdemjegy[0]
osztaly.pop(-1)
adatok.remove(adatok[0])
print(erdemjegy)
print(osztaly)
print(adatok)
print()

lst = [21,32,13,44,75]
x = int(input('Melyik számot szeretnéd módosítani?'))
y = int(input('Mi legyen az új szám?'))

index = x - 1

if index >= len(lst) or index < 0:
    print('Nincs ilyen elem')
else:
    lst[index] = y
    print(lst)
print()

lst.pop()

print(lst)

print(len(lst))

print()

for i in lst:
    print(i)

print()

elemek = int(input('Add meg az elemek számát: '))
lista = []
for i in range(elemek):
    szam = int(input('Kérlek adj meg egy számot:'))
    lista.append(szam)
print(lista)
lista.reverse()
print(lista)