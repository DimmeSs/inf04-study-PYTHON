def sort_wybierz():
    for i in range(len(numbers)):
        min_idx = i
        for j in range(i+1, len(numbers)):
            if numbers[min_idx] > numbers[j]:
                min_idx = j
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]


def sort_wstaw():
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i-1
        while j >= 0 and key < numbers[j]:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key


def sort_bubble():
    #numbers = [5 ,4 ,3 ,5 ,1]
    temp = 0
    sortowanie = True
    while sortowanie == True:
        sortowanie = False
        for i in range(len(numbers) - 1 - temp):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i+1] = numbers[i + 1], numbers[i]
                sortowanie = True
    temp += 1


# Użytkownik wybiera sposób sortowania
print("Wybierz sposób sortowania:")
print("1 - sortowanie przez wybieranie")
print("2 - ssortowanie przez wstawianie")
print("3 - sortowanie bombelkowe")
choice = int(input())

# Użytkownik wpisuje 5 liczb
numbers = []
print("Wprowadź pięć liczb oddzielonych spacją:")
numbers = [int(x) for x in input().split()]

if choice == 1:  # Sortowanie przez wybieranie
    sort_wybierz()
elif choice == 2:
    sort_wstaw()  # Sortowanie przez wstawianie
elif choice == 3:
    sort_bubble()  # Sortowanie bombelkowe

print("Posortowane liczby:")
for i in numbers:
    print(i, end=" ")
print()
end = input("wcisnij enter")
