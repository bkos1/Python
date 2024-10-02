text = "apple"
darab = 0
for i in range(len(text)):
    if text[i] in "aeiouAEIOU":
        darab += 1
print(f"A szövegben {darab} magánhangzó van.")


darab = 0
for x in text:
    if x.lower() in "aeiou":
        darab += 1
print(f"A szövegben {darab} magánhangzó van.")