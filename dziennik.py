
przedmioty = ["J.Polski", "Matematyka", "J.Angielski"]
oceny = [[],[],[],[],[],[],[],[],[],[]]
ilosc_ocen = 0
print("\n\n\n\n\n\n\n\n")
petla = False
while petla==False:
    Sum = 0
    if ilosc_ocen != 0:
        
        for j in range(10):
            Sum = Sum + sum(oceny[j])
        ogsr = Sum / ilosc_ocen
        print("srenia ogolna wynosi: " + str(round(ogsr, 2)) + "\n")

    for i in range(len(przedmioty)):
        
        b = i
        if len(oceny[i])>0:
            srednia = sum(oceny[i])/len(oceny[i])
            print(str(i+1) + " "+ str(przedmioty[i]))
            print(oceny[i])
            print("Srednia wynosi: "+str(round(srednia, 2)))
            print("")
        else:
            print(str(i+1) + " "+ str(przedmioty[i]))
            print("")

    print(str(len(przedmioty)+1) + " Dodanie przedmiotu\n")
    a = int(input("Wybierz liczbe odpowiadajaca przedmiotowi by dodac ocene lub dodaj przedmiot:\n"))
    if a > (len(przedmioty)+1) or a < 1:
        print("\n\n\n\n\n\n\n\n")
        print("nie ma takiego indeksu")
        print("\n")
    elif a == len(przedmioty)+1:
        nowy = input("Wpisz nazwe przedmiotu:\n")
        przedmioty.append(nowy)
        print("\n\n\n\n\n\n\n\n")
    else:
        ocena = int(input("Podaj ocene: "))
        while ocena > 6 or ocena < 1:
            ocena = int(input("Nieprawidlowe dane, prosze podac ocene jeszcze raz: "))
        oceny[a-1].append(ocena)
        ilosc_ocen = ilosc_ocen + 1
        print("\n\n\n\n\n\n\n\n")
    



    







        