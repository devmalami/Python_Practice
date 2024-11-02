while True:
    try:
        # Get and store user input for age 
        age = int(input("What is your age?: "))

        # Get and store user input for invitation status
        invite_status = input("Are you invited? (yes/no): ").lower()

        # Check if age is equal or greater than 18 and is invited
        if age >= 21 or invite_status == "yes":
            # Print if condition is TRUE
            print("You can attend the event")
        else:
            # Print if condition is FALSE
            print("Sorry, you cannot attend the event")
        break    
    except ValueError:
        print("Please input a valid answer")          
