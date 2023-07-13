file_path = r"D:\Programowanie\ZeroToJunior\100dni\Pliki_do_zadan\067.txt"

f = open(file_path, "w")

try:
    f.write("Wpisujemy tutaj linijke kodu i kasujemy jego zawartośc")
finally:
    f.close()
    
#Zadanie
#Stwórz plik todo.txt. Następnie napisz program, który pobierze od użytkownika 
#listę zadań do zrobienia (np. zakupy, sprzątanie, pranie itp.) i zapisze je do tego pliku (rozszerzając ten plik o nowe zadania, bez kasowania starych).

file_path1 = r"D:\Programowanie\ZeroToJunior\100dni\Pliki_do_zadan\067_1.txt"

f1 = open(file_path1, "a")

text = input("Enter a exercise you want to do: ")

try:
    f1.write(text)
    print(f1.readline())
finally:
    f1.close()
