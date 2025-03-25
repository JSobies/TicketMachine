import json

with open("prices.json", "r", encoding="UTF-8") as file:
    prices = json.load(file)

def display_menu(menu):
    print("Jaką opcję biletu chcesz kupić?")
    options = list(menu.keys())
    for index, option in enumerate(options):
        print(f"{index} - {option}")
    try:
        choice = int(input("Wybór: "))
    except TypeError:
        print("Wprowaadzono niepoprawny typ wartości. ")
    if choice > len(options)-1 or choice < 0:
        raise ValueError("Wprowadzono błędny numer opcji.")
    menu = menu[options[choice]]
    if isinstance(menu ,dict):
        return display_menu(menu)
    else:
        return (option, menu)
    

print(display_menu(prices))
#print("Jaką opcję biletu chcesz kupić?")
#options = list(prices.keys())
#for index, option in enumerate(options):
#    print(f"{index} - {option}")
#try:
#    choice = input("Wybór: ")
#except TypeError:
#    print("Wprowaadzono niepoprawny typ wartości. ")
#if choice > len(options)-1 or choice < 0:
#    raise ValueError
#menu = prices[option]
#print(choice)

#print(type(prices))
#print(json.dumps(prices, indent=4, ensure_ascii=False))
#print("Jaki rodzaj biletu chcesz kupić? ")
#for i in range(1,len(list(prices.keys()))+1):
#    print(f"{i} - {list(prices.keys())[i-1]}")
#for i in list(prices.keys()):
#print(*list(prices.keys()), sep="\n")