def nwd(x, y): #definiujemy funkcje do późniejszego użycia
    z = x % y if (x > y) else y % x # obliczamy reszte dzielenia z liczb (wykorzystujemy tu wyrażenie warunkowe)
    if z == 0:
        return y if (x > y) else x #jeżeli reszta ta jest rowna 0, to wynikiem jest mniejsza z liczb
    return nwd(z, y) if x > y else nwd(z, x) # w przeciwnym wypadku rekurencyjnie sprawdzamy NWD reszty dzielenia z mniejsza liczba
 
def nww(x, y):
  return x*y / nwd(x, y)

s = 0
print("Program znajdujacy najwiekszy wspolny dzielnik dwoch liczb")
print("Podaj liczbę a: ")
a = int(input())
print("Podaj liczbę b: ")
b = int(input())
while s == 0:
    w = input("----------\nCo chcesz obliczyć ? \n\n[1] = NWD \n[2] = NWW\n----------\n")
    if w == str(1):
        print("\n"+ str(nwd(a,b)))
        s +=1
    elif w == str(2):
        print("\n",str(nww(a,b)))
        s +=1
    else:
        print("[Error] Wpisz ponownie")



