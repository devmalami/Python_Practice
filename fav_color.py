try: 
    # Ask user to enter their name and favorite color

    # Take input for name
    name = input("What is your name?\n").title()

    # Take input for favorite color
    fav_color = input("What is your favorite color\n").title()
    
    # Print user's name and favorite color
    print(f"{name} likes {fav_color}")
except TypeError:
     print("Please enter a valid answer")
