# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a

# x= int(input("Podaj pierwszą liczbę:\n"))
# y= int(input("Podaj drugą liczbę:\n"))
# print("Twoje NWD wynosi :",gcd(x, y))

def NWD(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

x= int(input("Podaj pierwszą liczbę:\n"))
y= int(input("Podaj drugą liczbę:\n"))
print(NWD(x,y))