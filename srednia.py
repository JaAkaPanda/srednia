typ = int(input('Jaka srednia chcesz policzyc (Wpisz "1" dla arytmetyczna lub "2" dla wazona): '))
if typ != 1 and typ != 2:
    print("Błąd wyboru! Spróbuj ponownie!")
else:
    liczba_ocen = int(input("Enter the number of grades: "))
    oceny = ()
    wagi = ()
    suma_ocen = 0
    suma_wag = 0
    iloczyn = 0
    z = 0
    srednia = 0

    if typ == 2:
        for i in range(1, liczba_ocen+1):
            ocena = float(input("Wprowadz ocene: "))
            lista_ocen = list(oceny)
            lista_ocen.append(ocena)
            oceny = tuple(lista_ocen)
            waga = int(input("Wprowadz wage oceny: "))
            lista_wag = list(wagi)
            lista_wag.append(waga)
            wagi = tuple(lista_wag)
        for i in oceny:
            o = wagi[z]
            suma_ocen += i * o
            z += 1 
        for i in wagi:
            suma_wag += i
        if suma_wag <= 0:
            print("Bledna suma wag. Brak wyniku.")
        else:
            srednia = suma_ocen/suma_wag
    elif typ == 1:
        for i in oceny:
            o = wagi[z]
            suma_ocen += i * o
            z += 1
            srednia = suma_ocen/liczba_ocen
print("Twoja srednia wynosi: ", srednia)
