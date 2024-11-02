while True:
    try:
        age = int(input("Enter your age: "))
        country = (input("Enter your country: "))
        if age >= 18 and country == "Nigeria":
            print("\nYou are admitted!")
        else:
            print("\nYou cannot be admitted.")
        break
    except ValueError:
            print("Pleae enter valid answers\n")
