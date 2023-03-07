# Import wymaganych modułów
from tkinter import *
from tkinter import ttk
from tkinter import font
from math import *
from statistics import *

# Okno główne programu (MASTER)
window = Tk()
window.title('_Kalkulator_')
window.iconbitmap(r'img.ico')
window.resizable(False,False)

# Style
ttk.Style().configure('Dark.TFrame', foreground='silver', background='#1a3558')

# Zmiana czcionki domyślnej
mainFont = font.Font(family='Calibri', name='appFont', size=28, weight='normal')

# Śledzenie aktualnej pozycji w wejściowym polu tekstowym
i = 0

# Otrzymuje cyfrę jako parametr i wyświetla ją w polu wejściowym
def get_variables(num):
    global i
    display.insert(i,num)
    i+=1
 
# Funkcja Calculate skanuje ciąg, aby go ocenić i wyświetlić
def calculate():
    entire_string = display.get()
    recording(entire_string)
    try:
        a = entire_string
        result = round(eval(a), 6)
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0,"Błąd danych")

# Zapis wykonanej operacji do pliku tekstowego
def recording(txt):
  file = open("historyCalc.txt", "a")
  file.write(str(txt) + "=" + str(round(eval(txt), 6)) + "\n")
  file.close()
 
# Funkcja, która przyjmuje operator jako dane wejściowe i wyświetla go w polu wejściowym
def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i,operator)
    i+=length
 
# Funkcja czyszcząca pole wejściowe
def clear_all():
    display.delete(0,END)
 
# Funkcja, która usuwa ostatni znak z pola wejściowego
def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0,new_string)
    else:
        clear_all()
        display.insert(0,"Błąd danych")

# Funkcja obliczania silni i wyświetlania jej;
def fact():
    entire_string = display.get()
    try:
        result = factorial(int(entire_string))
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0,"Błąd danych")

#--------------------------------------UI Design ---------------------------------------------

# Okno intefejsu programu (SLAVE)
mainFrame = ttk.Frame(window, style='Dark.TFrame', padding=10)
mainFrame.grid(column=0, row=0, sticky=N+S+E+W)

# Okno wyświetlacza danych i wyników
display = Entry(mainFrame, font=mainFont, background='#9aebfb')
display.grid(row=0, column=0, columnspan=8, ipady=5, pady=(0,40), sticky=N+S+E+W)

# Kod dodawania przycisków do Kalkulatora
Button(mainFrame, text="7", activebackground='#0ff', font=mainFont, command = lambda :get_variables(7)).grid(row=1, column=0, padx=5, pady=5, sticky=N+S+E+W)
Button(mainFrame, text="8", activebackground='#0ff', font=mainFont, command = lambda :get_variables(8)).grid(row=1, column=1, padx=5, pady=5, sticky=N+S+E+W)
Button(mainFrame, text="9", activebackground='#0ff', font=mainFont, command = lambda :get_variables(9)).grid(row=1, column=2, padx=5, pady=5, sticky=N+S+E+W)

Button(mainFrame, text="4", activebackground='#0ff', font=mainFont, command = lambda :get_variables(4)).grid(row=2, column=0, padx=5, pady=5, sticky=N+S+E+W)
Button(mainFrame, text="5", activebackground='#0ff', font=mainFont, command = lambda :get_variables(5)).grid(row=2, column=1, padx=5, pady=5, sticky=N+S+E+W)
Button(mainFrame, text="6", activebackground='#0ff', font=mainFont, command = lambda :get_variables(6)).grid(row=2, column=2, padx=5, pady=5, sticky=N+S+E+W)

Button(mainFrame, text="1", activebackground='#0ff', font=mainFont, command = lambda :get_variables(1)).grid(row=3, column=0, padx=5, pady=5, sticky=N+S+E+W)
Button(mainFrame, text="2", activebackground='#0ff', font=mainFont, command = lambda :get_variables(2)).grid(row=3, column=1, padx=5, pady=5, sticky=N+S+E+W)
Button(mainFrame, text="3", activebackground='#0ff', font=mainFont, command = lambda :get_variables(3)).grid(row=3, column=2, padx=5, pady=5, sticky=N+S+E+W)

Button(mainFrame, text="0", activebackground='#0ff', font=mainFont, command = lambda :get_variables(0)).grid(row=4, columnspan=2, padx=5, pady=5, sticky=N+S+E+W)
Button(mainFrame, text=",", activebackground='#0ff', font=mainFont, command = lambda :get_variables(".")).grid(row=4, column=2, padx=5, pady=5, sticky=N+S+E+W)

Button(mainFrame, text="DEL", background='#0062b7', foreground='#fff', activebackground='#0062b7', font=mainFont, command = lambda :clear_all()).grid(row=1, column=4, columnspan=2, padx=(20, 5), pady=5, sticky=N+S+E+W)
Button(mainFrame, text="AC", background='#0062b7', foreground='#fff', activebackground='#0062b7', font=mainFont, command = lambda :undo()).grid(row=1, column=6, columnspan=2, padx=5, pady=5, sticky=N+S+E+W)

Button(mainFrame, text="+", activebackground='#0ff', font=mainFont, command = lambda :get_operation("+")).grid(row=2, column=4, padx=(20, 5), pady=5, sticky=N+S+E+W)
Button(mainFrame, text="−", activebackground='#0ff', font=mainFont, command = lambda :get_operation("-")).grid(row=2, column=5, padx=5, pady=5, sticky=N+S+E+W)
Button(mainFrame, text="π", background='#0062b7', activebackground='#0062b7', font=mainFont, command = lambda :get_operation("pi")).grid(row=2, column=6, padx=5, pady=5, sticky=N+S+E+W)
Button(mainFrame, text="e", background='#0062b7', activebackground='#0062b7', font=mainFont, command = lambda :get_operation("e")).grid(row=2, column=7, padx=5, pady=5, sticky=N+S+E+W)

Button(mainFrame, text="×", activebackground='#0ff', font=mainFont, command = lambda :get_operation("*")).grid(row=3, column=4, padx=(20, 5), pady=5, sticky=N+S+E+W)
Button(mainFrame, text="÷", activebackground='#0ff', font=mainFont, command = lambda :get_operation("/")).grid(row=3, column=5, padx=5, pady=5, sticky=N+S+E+W)
Button(mainFrame, text="%", activebackground='#0ff', font=mainFont, command = lambda :get_operation("%")).grid(row=3, column=6, padx=5, pady=5, sticky=N+S+E+W)
Button(mainFrame, text="!", activebackground='#0ff', font=mainFont, command = lambda :fact()).grid(row=3, column=7, padx=5, pady=5, sticky=N+S+E+W)

Button(mainFrame, text="(", activebackground='#0ff', font=mainFont, command = lambda :get_operation("(")).grid(row=4, column=4, padx=(20, 5), pady=5, sticky=N+S+E+W)
Button(mainFrame, text=")", activebackground='#0ff', font=mainFont, command = lambda :get_operation(")")).grid(row=4, column=5, padx=5, pady=5, sticky=N+S+E+W)
Button(mainFrame, text="=",background='#0062b7', activebackground='#0062b7', font=mainFont, command = lambda :calculate()).grid(row=4, column=6, columnspan=2, padx=5, pady=5, sticky=N+S+E+W)

# Label info
lblInfo = ttk.Label(mainFrame, text='(C) 2023 Szymon Słoniowski - Elektronik \nProfil nauczania: technik programista' ,foreground='silver',background='#1a3558', justify='center', padding=(0, 20,0,10))
lblInfo.grid(column=0, row=5, columnspan=8)

# Pętla programu
window.mainloop()
