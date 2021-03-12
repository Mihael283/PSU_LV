status = 0
sum = 0
i = 0
max = -2147483647
min = 2147483647

srednja_vrijednost = 0
print("Unesite brojeve. Ako zelite izaci upisite \"Done\"")
while status == 0:
    try:
        user = input()
        a = int(user)
        sum += a
        i += 1
        if a > max:
            max = a
        if a < min:
            min = a
    except ValueError: 
        if user == "Done":
            status = 1
            break
        print("Molim vas unesite ili broj ili \"Done\"")
srednja_vrijednost = sum/i
print("Ukupno brojeva: ", i)
print("Srednja vrijednost brojeva: ", srednja_vrijednost)
print("Najveci broj: ", max)
print("Najmanji broj: ", min)