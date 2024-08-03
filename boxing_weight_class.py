
def Boxing():
    w = float(input("Enter the weight in lbs: "))
    x = input("Are you a man or woman: ")
    kg = w/2.2046
    kg = round(kg,1)

    if x == "man":
        print("Olympic Men's boxing")
        if kg <= 49:
            print("kg:", kg)
            print("Light Flyweight")
        elif kg <= 52:
            print("kg:", kg)
            print("Flyweight")
        elif kg <= 56:
            print("kg:", kg)
            print("Bantamweight")
        elif kg <= 60:
            print("kg:", kg)
            print("Lightweight")
        elif kg <= 64:
            print("kg:", kg)
            print("Light Welterweight")
        elif kg <= 69:
            print("kg:", kg)
            print("Welterweight")
        elif kg <= 75:
            print("kg:", kg)
            print("Middle weight")
        elif kg <= 81:
            print("kg:", kg)
            print("Light Heavyweight")
        elif kg <= 91:
            print("kg:",kg)
            print("Heavyweight")
        else:
            print("kg:", kg)
            print("Super Heavyweight")

    if x == "woman":
        print("Olympic Women's boxing")
        if kg <= 48:
            print("kg:",kg)
            print("Light Flyweight")
        elif kg <= 51:
            print("kg:",kg)
            print("Flyweight")
        elif kg <= 54:
            print("kg:",kg)
            print("Bantamweight")
        elif kg <= 57:
            print("kg:",kg)
            print("Featherweight")
        elif kg <= 60:
            print("kg:",kg)
            print("Lightweight")
        elif kg <= 64:
            print("kg:",kg)
            print("Welterweight")
        elif kg <= 69:
            print("kg:",kg)
            print("Light Middleweight")
        elif kg <= 75:
            print("kg:",kg)
            print("Middleweight")
        elif kg <= 81:
            print("kg:",kg)
            print("Light Heavyweight")
        else:
            print("kg:",kg)
            print("Heavyweight")

Boxing()
