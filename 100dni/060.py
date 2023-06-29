#dzien 60
#Zadanie

#Przed Tobą lista produktów, które trzeba kupić.

#jajka, mleko, chleb, jajka, masło, jajka, jabłka, chleb

#Przygotuj aplikację która.

#Będzie miała wbudowany cennik wszystkich produktów.
#Przygotuje listę zakupów, złożoną z unikalnych produktów oraz podanej obok liczby produktów do kupienia.
#Wyliczy wartość zakupów i poda ją w podsumowaniu.
#Na moje oko, przyda Ci się lista, słownik i zbiór :)

shopping_list = set()
shopping_list_quatity = {}
total_price = []
price_list_of_products = {
    "mleko" : 5,
    "masło" : 4,
    "chleb" : 2,
    "jajka" : 10,
    "jabłka" : 3
}

def add_product_to_shopping_list():
    while True:
        product = input("enter your product to but.If you want to end your list press enter: ")
        if product == "":
            break
        else:
            shopping_list.add(product)

def get_quantity():
    for product in shopping_list:
        quantity = int(input(f"Enter quantity of {product}: "))
        shopping_list_quatity[product] = quantity
        
def print_shopping_list():
    print("Your shopping list")
    for product in shopping_list_quatity:
        print(product, shopping_list_quatity[product])
        print(shopping_list)
        print(shopping_list_quatity)

def print_total_cost():
    for item in shopping_list_quatity:
        if item in price_list_of_products:
            total_price.append(price_list_of_products[item] * shopping_list_quatity[item])
        else:
            continue
    print(f"Total cost of the groceries I have the prices of is: {sum(total_price)}zł")

        



def make_program():
    add_product_to_shopping_list()
    get_quantity()
    print_shopping_list()
    print_total_cost()
    
make_program()
