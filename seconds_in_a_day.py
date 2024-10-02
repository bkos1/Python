currentHours = int(input("Add meg az órát: "))
currentMinutes = int(input("Add meg a percet: "))
currentSeconds = int(input("Add meg a másodpercet: "))
x = 60 * 60 * currentHours + 60 * currentMinutes + currentSeconds
nap = 60*60*24
y = nap - x
print(f"Hátralévő másodpercek: {y} sec")