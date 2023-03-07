import random

def fill_array(arr):
    for i in range(len(arr)):
        arr[i] = random.randint(1, 100)

def search_array(arr, x):
    arr.append(x) # dodajemy wartownika
    for i in range(len(arr)):
        if arr[i] == x:
            if i == len(arr)-1: # sprawdzamy czy trafiliśmy na wartownika
                return None
            else:
                return i

if __name__ == "__main__":
    arr = [0] * 50
    fill_array(arr)
    x = int(input("Podaj wartość do wyszukania: "))
    index = search_array(arr, x)
    if index is None:
        print("Nie znaleziono elementu.")
    else:
        print("Znaleziono element na pozycji: ", index)
    print("Zawartość tablicy: ", arr)