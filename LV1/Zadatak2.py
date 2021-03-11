try:
    inp = input("Unesite broj između 0 i 1: ")
    score = float(inp)
    if (score >= 1.0):
        print("Pogrška u unosu,unesite broj između 0 i 1!")
        exit()
    elif (score >= 0.9):
        print("A")
    elif (score >= 0.8):
        print("B")
    elif (score >= 0.7):
        print("C")
    elif (score >= 0.6):
        print("D")
    else:
        print("F") 
except:
    print("Molimo unesite broj!")
    exit()