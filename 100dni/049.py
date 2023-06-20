#dzien 39

dict = {
    "imie": "Daniel",
    "nazwisko": "Nowak",
    "rok": 1990
}

#fix it

def check_key(value, dict):
    if value in dict:
        return True
    return False

print(check_key("imie", dict))
print(check_key("waga", dict))


dict.pop("rok")
print(dict)


#Zdanie 
#Stwórz program, który będzie przechowywał słownik z nazwami państw i ich stolicami. 
#Następnie poproś użytkownika o podanie nazwy państwa, a program ma wyświetlić stolicę tego państwa. Jeśli użytkownik poda nazwę państwa, 
#której nie ma w słowniku, program powinien wyświetlić komunikat o błędzie.

def print_country(country, dict):
    if country in dict:
        return dict[country]
    else:
        return "Country doesnt exit in dictionary"
    


countries = {"Polska": "Warszawa", "Niemcy": "Berlin", "Francja": "Paryż", "Włochy": "Rzym"}

country_name = input("Enter a country: ")
print(print_country(country_name, countries))

