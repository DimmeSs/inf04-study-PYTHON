import random

pesele = []
Ppesele = []


def CzyGit():
    lPpeseli = 0
    for i in range(50):
        wordlist = ''
        wordlist = list(pesele[i])
        wynik = int(wordlist[0])*1+int(wordlist[1])*3+int(wordlist[2])*7+int(wordlist[3])*9+int(wordlist[4])*1+int(wordlist[5])*3+int(wordlist[6])*7+int(wordlist[7])*9+int(wordlist[8])*1+int(wordlist[9])*3
        toList = list(str(wynik))
        lastOne = int(toList[len(toList)-1])
        check = 10 - lastOne
        if check == int(wordlist[len(wordlist)-1]):
            Ppesele.append(pesele[i])
            lPpeseli += 1
    return lPpeseli

def sprawdzGender():
    Genders = []
    nWoman = 0
    nMan = 0
    for i in range(len(Ppesele)):
        wordlist = ''
        wordlist = list(Ppesele[i])
        if int(wordlist[9])%2 == 0:
            nWoman += 1
        else:
            nMan += 1
    Genders.append(nMan)
    Genders.append(nWoman)
    return Genders

def RandomPesel():
    pesel = ''
    for i in range(50):
        pesel = ''
        for z in range(11):
            pesel = pesel + str(random.randint(0, 9))
        pesele.append(pesel)
    return

def main():
    Genders = []
    RandomPesel()
    licz = CzyGit()
    print("Wygenerowane Pesele :\n\n",pesele);print("\nPoprawna lista ["+ str(licz)+"] Peseli :\n",Ppesele)
    Plec = sprawdzGender()
    print("Ilość Męskich Peseli [" + str(Plec[1])+"]")
    print("Ilość Żeńskich Peseli [" + str(Plec[0])+"]")
    input("\nWciśnij [Enter] Aby zakończyć program")
main()