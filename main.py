from functions import *

# wczytanie danych z pliku
file = open('ml.csv', 'r').read()


#zapis do tabeli
tabela = zapis(file)

#ilość powtórzeń
dict = ilosc_wystapien(tabela)
print(dict.items())