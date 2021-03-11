Satnica = input("Unesite iznosi koji dobivate po radnom satu:") 
Radni_sati = input("Unesite broj radnih sati:")


def ispis_zarade():
    print("Placa po satu:",Satnica)
    print("Broj radnih sati:",Radni_sati)
    Zarada=(int(Satnica)*int(Radni_sati))
    print(Zarada)

ispis_zarade()