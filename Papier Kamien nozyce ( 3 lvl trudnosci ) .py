import random
import time
import os

print(" // Witaj W Grze papier kamień nożyce \\\ \nWpisz poniżej liczbe która definiuje jaki tryb gry chcesz grać :")
s = True
pc = ""
Szansa = None
Chce = True
Chcee = True
#def pcLOST(w):
 #   if w == "KAMIEN":
  #      pc = "NOZYCE"
  #  elif w == "PAPIER":
  #      pc = "KAMIEN"
   # elif w == "NOZYCE":
   #     pc = "PAPIER"
#def pcWIN(self):
 #   if w == "KAMIEN":
 #       pc = "PAPIER"
 #   elif w == "PAPIER":
#       pc = "NOZYCE"
 #   elif w == "NOZYCE":
  #      pc = "KAMIEN"
#---------------------------#TRYB ŁATWY#------------------------------
def graone():
    Chce = True
    pc = ""
    Chcee = True
    while Chce == True:
        
        Xd = True
        while Xd == True:
            w = input("Wpisz swoją odpowiedź ( Kamien / Papier / Nozyce ) xX Bez Polskich Znaków Xx\n").upper()
            if len(w) == 6:
                Xd = False
            elif len(w)> 6 or len(w)<6:
                print("----------------------\nWpisz poprawną rzecz\n-----------------------------")
                Xd = True
        Szansa =  random.randint(1,7)#np 4
        #Jeżeli 2 to remis | 1 Przegrałeś | 3-7 Wygrałeś
        p = "PAPIER"
        k = "KAMIEN"
        n = "NOZYCE"

        if Szansa == 2:
            print("------------------------------------\nWpisałeś:",w,"\n=> Komputer Wpisuuje swoją odpowiedź <=\n# WYNIK #")
            Szansa = w
            time.sleep(2)
            print("# REMIS #\nKomputer wybrał",w)
            Chcee = True

        elif Szansa == 1:
            pc = ""
            if w == "KAMIEN":
                pc = "PAPIER"
            elif w == "PAPIER":
                pc = "NOZYCE"
            elif w == "NOZYCE":
                pc = "KAMIEN"
            print("------------------------------------\nWpisałeś:",w,"\n=> Komputer Wpisuuje swoją odpowiedź <=\n# WYNIK #")
            time.sleep(2)
            print("# Przegrałeś #\nKomputer wybrał",pc)
            Chcee = True

        elif Szansa > 2 and Szansa <= 7:
            pc = ""
            if w == "KAMIEN":
                pc = "NOZYCE"
            elif w == "PAPIER":
                pc = "KAMIEN"
            elif w == "NOZYCE":
                pc = "PAPIER"
            print("------------------------------------\nWpisałeś:",w,"\n=> Komputer Wpisuuje swoją odpowiedź <=\n# WYNIK #")
            time.sleep(2)
            print("# Wygrałeś #\nKomputer wybrał",pc)
            Chcee = True

        while Chcee == True:
            chc = input("-------------------\nTry Again ? y/n\n").lower()

            if chc == "n":
                Chce = False
                Chcee = False

            elif chc == "y":
                Chcee = False
                Chce = True
                os.system('cls')
                
            else:
                print("Wpisz Ponownie")
                Chcee = True
        

#---------------------------#TRYB TRUDNY#------------------------------
def gratwo():
    Chce = True
    pc = ""
    Chcee = True
    while Chce == True:
        w = input("Wpisz swoją odpowiedź ( Kamien / Papier / Nozyce ) xX Bez Polskich Znaków Xx\n").upper()
        Szansa =  random.randint(1,4)#np 2
        #Jeżeli 1 to remis | 2-3 Przegrałeś | 4 Wygrałeś
        p = "PAPIER"
        k = "KAMIEN"
        n = "NOZYCE"

        if Szansa == 1:
            print("------------------------------------\nWpisałeś:",w,"\n=> Komputer Wpisuuje swoją odpowiedź <=\n# WYNIK #")
            Szansa = w
            time.sleep(2)
            print("# REMIS #\nKomputer wybrał",w)
            Chcee = True

        elif Szansa == 2 or Szansa == 3:
            pc = ""
            if w == "KAMIEN":
                pc = "PAPIER"
            elif w == "PAPIER":
                pc = "NOZYCE"
            elif w == "NOZYCE":
                pc = "KAMIEN"
            print("------------------------------------\nWpisałeś:",w,"\n=> Komputer Wpisuuje swoją odpowiedź <=\n# WYNIK #")
            time.sleep(2)
            print("# Przegrałeś #\nKomputer wybrał",pc)
            Chcee = True

        elif Szansa == 4:
            pc = ""
            if w == "KAMIEN":
                pc = "NOZYCE"
            elif w == "PAPIER":
                pc = "KAMIEN"
            elif w == "NOZYCE":
                pc = "PAPIER"
            print("------------------------------------\nWpisałeś:",w,"\n=> Komputer Wpisuuje swoją odpowiedź <=\n# WYNIK #")
            time.sleep(2)
            print("# Wygrałeś #\nKomputer wybrał",pc)
            Chcee = True

        while Chcee == True:
            chc = input("-------------------\nTry Again ? y/n\n").lower()

            if chc == "n":
                Chce = False
                Chcee = False

            elif chc == "y":
                Chcee = False
                Chce = True
                os.system('cls')
            else:
                print("-----\nWpisz Poprawną odpowiedź!")
                Chcee = True
        
#---------------------------#TRYB NIEMOŻLIWY#------------------------------
def gratri():
    Chce = True
    pc = ""
    Chcee = True
    while Chce == True:
        w = input("Wpisz swoją odpowiedź ( Kamien / Papier / Nozyce ) xX Bez Polskich Znaków Xx\n").upper()
        Szansa =  random.randint(1,2)#np 2
        #Jeżeli 1 to remis | 2 Przegrałeś | 3 Wygrałeś XD
        p = "PAPIER"
        k = "KAMIEN"
        n = "NOZYCE"

        if Szansa == 1:
            print("------------------------------------\nWpisałeś:",w,"\n=> Komputer Wpisuuje swoją odpowiedź <=\n# WYNIK #")
            Szansa = w
            time.sleep(2)
            print("# REMIS #\nKomputer wybrał",w)
            Chcee = True

        elif Szansa == 2:
            pc = ""
            if w == "KAMIEN":
                pc = "PAPIER"
            elif w == "PAPIER":
                pc = "NOZYCE"
            elif w == "NOZYCE":
                pc = "KAMIEN"
            print("------------------------------------\nWpisałeś:",w,"\n=> Komputer Wpisuuje swoją odpowiedź <=\n# WYNIK #")
            time.sleep(2)
            print("# Przegrałeś #\nKomputer wybrał",pc)
            Chcee = True

        while Chcee == True:
            chc = input("-------------------\nTry Again ? y/n\n").lower()

            if chc == "n":
                Chce = False
                Chcee = False

            elif chc == "y":
                Chcee = False
                Chce = True
                os.system('cls')
                
            else:
                print("-----\nWpisz Poprawną odpowiedź!")
                Chcee = True
        
while s == True:
    pocz = input("---------------------\n[1] Łatwy\n[2] Trudny\n[3] Niemożliwy\n---------------------\n")
    try:#sprawdza formułke jeżeli wpisana rzecz == str to normalnie wywali bład przez co musisz użyć except ( nazwa bledu ) żeby zamiast wylaczyć program zrobi coś innego
        pocz = int(pocz)
        if pocz > 3 or pocz < 1: raise ValueError
    except ValueError:
        print("\n[Error Wpisz Ponownie Liczbe Error]")
        
    if pocz == 1:
        graone()
        s = False
    elif pocz == 2:
        gratwo()
        s = False
    elif pocz == 3:
        gratri()
        s = False
        

    
