#dzien 70
import requests

url =  'https://example.com/plik_tekstowy.txt'
response = requests.get(url)

if response.status_code == 200:
    # Odczytaj zawartość pliku, uwzględniając odpowiednie kodowanie znaków
    text = response.content.decode('UTF-8', errors='ignore')
    print("Pobrany tekst:")
    print(text)
else:
    print(f"Błąd pobierania pliku: {response.status_code}")