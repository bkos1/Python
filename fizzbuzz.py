for i in range(1, 51):
    kiirando = ""
    if i % 3 == 0:
        kiirando = "fizz"
    if i % 5 == 0:
        kiirando += "buzz"
    if kiirando == "":
        kiirando = i
    print(kiirando, end=", ")