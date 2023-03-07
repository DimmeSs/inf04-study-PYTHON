numb = 0
for ilosc in range(1,21):
    numb +=1
    if numb == 3 or numb == 13: answ = "UNLUCKY"
    elif numb % 2 == 0:answ = "even"
    else: answ = "odd"
    print(numb,"is",answ)
input("Wciśnij enter aby zakończyć")
