while True:
    try:
        age = int(input("Enter your age: "))

        if age >= 18:
            print("Congrats! You are an adult and eligible\n")
        else:
            print("Sorry you are a minor and not eligible\n")
        break    
    except ValueError:
        print("Please enter numerals only\n")
