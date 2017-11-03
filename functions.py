# ZAPIS DANYCH DO LISTY
def zapis(file):
    tabela = []
    lines = file.split('\n')
    for line in lines:
        tabela.append(line.split(','))
    return tabela

# ILOŚĆ POWTÓRZEŃ WYLOSOWANYCH LICZB W KOLEJNYCH LOSOWANIACH
def ilosc_wystapien(tabela):
    dict = {}
    licznik = 0
    liczba = 1
    for liczba in range(1, 81):
        for linia in tabela:
            for numer in linia:
                numer = int(numer)
                if numer is liczba:
                    licznik += 1
                    break;
        # print(liczba, ' - ', licznik)
        dict[liczba] = licznik
        liczba += 1
        licznik = 0
    return dict

# def odstepy(liczba, tabela):
#     liczba = int(liczba)
#     licznik = 0
#     flaga = True
#     for linia in tabela:
#         for elem in linia:
#             if elem is liczba:
#                 licznik += 1
#                 break
#
#         print(licznik)