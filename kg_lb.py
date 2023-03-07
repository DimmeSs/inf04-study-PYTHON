while True:
    info = input("Twoja Waga: ")
    try:
        info = float(info)
        break
    except ValueError:
        print("Niepoprawna Waga.Wpisz ponownie")
    
while True:
    
    cecha = input("Podana Dana jest w czym ? \n[K] for kg || [L] for Lbs \n").upper()
    if cecha == "K":
        ik = info*2.20462262
        ik = round(ik,2)
        print("\nWaga w lbs = " + str(ik)) 
        break
    elif cecha == "L":
        ik = info/2.20462262
        ik = round(ik,2)
        print("Waga w kg = " + str(ik))
        break
    else:
        print("[ Error ]")
input("Wcisnij ENTER aby zakonczyć")































111*8