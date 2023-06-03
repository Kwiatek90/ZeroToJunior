#dzień 36
#Masz przez 3 tygodnie, wykonywać codziennie pięć konkretnych tasków.

#Zadanie A, Zadanie B, Zadanie C, Zadanie D i Zadanie E

#Przygotuj kod, który wypisze na ekranie listę zadań w następujący sposób.

#Dzień tygodnia - numer zadania - opis zadania

#1 - 1 - Zadanie A
#1 - 2 - Zadanie B
#1 - 3 - Zadanie C
#1 - 4 - Zadanie D
#1 - 5 - Zadanie E
#2 - 1 - Zadanie A
#2 - 2 - Zadanie B
#Itd

zadania = ["Zadanie A", "Zadanie B", "Zadanie C", "Zadanie D", "Zzadanie E"]

for i in range(1,6):
    j = 1
    while j <= 5:
        for zadanie in zadania:
            print(f"{i} - {j} - {zadanie}")
            j += 1
            
                


