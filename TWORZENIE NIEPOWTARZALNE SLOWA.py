import itertools
alphabet =[]
key = ''
while True:
    x = input("Wpisz 10 liter || Wciśnij [ENTER] aby zakończyć\n")
    for letters in x:
        alphabet.append(letters)

    a = set(alphabet)
    if len (a) < 10:
        print("znaki sie powtarzaja")
    else:
        break

licznik = 0
wordlist = []
string = ''
string = string.join(alphabet)
for x in itertools.permutations(sorted(string)):
    wordlist.append(x)
    print(*wordlist[licznik])
    licznik += 1
print("---------------------------\nUtworzono "+ str(licznik)+" niepowtarzalnych słów")
input("wcisnij ENTER aby zakończyć")
















































































 #   if len(alphabet)<10:
  #      print ("Wprowadzono za malo znakow")
  #  elif len(alphabet)>10:
  #      print ("Za duzo znakow")
   # else:
  #      print("wprowadzono odpowiednia ilosc znakow")
