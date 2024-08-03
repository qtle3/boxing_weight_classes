def get_gender():
    while True:
        x = input("Are you a man or woman: ")
        if x in ["man", "women"]:
            return x
        else:
            print("Invalid input. Please Type 'man' or 'woman'")


def Boxing():
    w = float(input("Enter the weight in lbs: "))
    x = get_gender()
    kg = w / 2.2046
    kg = round(kg, 1)

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

    women_weight_classes = [
        (51, "Flyweight"),
        (57, "Featherweight"),
        (60, "Lightweight"),
        (69, "Welterweight"),
        (75, "Middleweight"),
    ]

    if x == "man":
        print("Olympic Men's boxing")
        for weight, weight_class in men_weight_classes:
            if kg <= weight:
                print("kg:", kg)
                print(weight_class)
                break

    if x == "woman":
        print("Olympic Women's boxing")


Boxing()
