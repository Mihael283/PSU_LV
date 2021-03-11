i=0
max=0
min=0

number = 1
while number > 0:
    try:
        number = int(input('Enter a positive number: '))
    if number > 0:
        if variable>max:
            max=variable
        elif variable<min:
            min=variable
    except ValueError:
        print("Ponovite unos")
        continue

