teljes = float(input("Kérlek add meg a teszt pontszámát: "))
eredmény = float(input("kérlek add meg a kapott pontszámot: "))
jegy = (eredmény / teljes)*100
if jegy <= 50:
    print(f"A kapott osztályzat: E ({jegy})")
elif jegy > 50 and jegy <= 65:
    print(f"A kapott osztályzat: D ({jegy})")
elif jegy > 65 and jegy <= 75:
    print(f"A kapott osztályzat: C ({jegy})")
elif jegy > 75 and jegy <= 85:
    print(f"A kapott osztályzat: B ({jegy})")
elif jegy > 85 and jegy <= 99:
    print(f"A kapott osztályzat: A ({jegy})")
elif jegy == 100:
    print(f"A kapott osztályzat: A+ ({jegy})")
