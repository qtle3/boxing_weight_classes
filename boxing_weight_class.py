def get_gender():
    while True:
        x = input("Are you a man or woman: ")
        if x in ["man", "women"]:
            return x
        else:
            print("Invalid input. Please Type 'man' or 'woman'")


def Boxing():
    # Get the weight in lbs and gender from the user
    w = float(input("Enter the weight in lbs: "))
    x = get_gender()
    # Convert the weight to kg
    kg = w / 2.2046
    kg = round(kg, 1)
    # men weight classes
    men_weight_classes = [
        (52, "Flyweight"),
        (57, "Featherweight"),
        (63, "Lightweight"),
        (69, "Welterweight"),
        (75, "Middleweight"),
        (81, "Light Heavyweight"),
        (91, "Heavyweight"),
        (float("inf"), "Super Heavyweight"),
    ]
    # women weight classes
    women_weight_classes = [
        (51, "Flyweight"),
        (57, "Featherweight"),
        (60, "Lightweight"),
        (69, "Welterweight"),
        (75, "Middleweight"),
    ]

    # Check if the user is a man and print the weight class
    if x == "man":
        print("Olympic Men's boxing")
        for weight, weight_class in men_weight_classes:
            if kg <= weight:
                print("kg:", kg)
                print(weight_class)
                break
    # Check if the user is a woman and print the weight class
    if x == "woman":
        print("Olympic Women's boxing")
        for weight, weight_class in women_weight_classes:
            if kg <= weight:
                print("kg:", kg)
                print(weight_class)
                break


Boxing()
