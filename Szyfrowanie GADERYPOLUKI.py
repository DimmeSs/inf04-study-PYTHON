cipher = {'G': 'A', 'A': 'G', 'D': 'E', 'E': 'D', 'R': 'Y', 'Y': 'R', 'P': 'O', 'O': 'P', 'L': 'U', 'U': 'L', 'K': 'I', 'I': 'K'}

# Pobieranie tekstu od użytkownika
plaintext = input("Wprowadź tekst do zaszyfrowania: ")
plaintext = plaintext.upper()
# Inicjalizacja zmiennej do przechowywania zaszyfrowanego tekstu
'''********************************************************
* nazwa funkcji: zmiana
* parametry wejściowe: tekst - tekst od użytkownika do szyfrowania
* wartość zwracana: Funkcja "zmiana" zwraca zaszyfrowany tekst
* autor: 4234234234324234
* ****************************************************'''
# Szyfrowanie tekstu dla każdej litery wykona się 1 for
def zmiana(plaintext):
    ciphertext = ""
    for ch in plaintext:
        # Jeśli litera jest w kluczu, to zamieniamy ją na odpowiadającą jej literę z klucza
        if ch in cipher:
            ciphertext += cipher[ch]
        # W przeciwnym razie pozostawiamy ją bez zmian
        else:
            ciphertext += ch
    return ciphertext
# Wyświetlenie zaszyfrowanego tekstu
print("Zaszyfrowany tekst:",zmiana(plaintext))

'''********************************************************
SCHEMAT
* nazwa funkcji: <tu wstaw nazwę funkcji>
* parametry wejściowe: <nazwa parametru> - <co przechowuje>
* wartość zwracana: <co zwraca funkcja – opis>
* autor: <numer PESEL zdającego>
* ****************************************************'''

