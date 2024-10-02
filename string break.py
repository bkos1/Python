text = input("Kérlek edj meg egy szöveget: ")
for x in text:
    if x.lower() in "aáeéiíoóöőuúűü":  
        break
    print(x, end=", ")