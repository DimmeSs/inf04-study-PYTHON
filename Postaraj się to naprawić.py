from re import T


s = True
while s == True:
    info = input("Weight: ")
    int(info)
    infos = type(info)
    if infos is str:
        print("error")
    else:
        s = False
k = True
while k == True:
    cecha = input("Podana Dana jest w czym ? \n[K] for kg || [L] for Lbs \n")
    if cecha.upper() == "K":
        ik = float(info)*0.45
        print("Waga w lbs = " + str(round(ik,2)))
        k = False
    elif cecha.upper() == "L":
        i = info/0.45
        print("Waga w kg = " + str(round(i,2)))
        k = False
    else:
        print("[ Error ]")
































111*8