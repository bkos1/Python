nap_sorszama= int(input("Kérlek add meg a nap számát: "))
match nap_sorszama:
      case 0 | 1 | 2 | 3 | 4: print("Munkanap")
      case 6 | 5: print("Hétvége")
      case _: print("Rossz napot adtál meg")