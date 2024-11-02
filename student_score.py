while True:
    try:
        score = int(input("Enter your score from 1-100: "))
        if score >= 90 and score <= 100:
            print('\nA')
            break
        elif score >= 80 and score <= 89:
            print('\nB')
            break
        elif score >= 70 and score <= 79:
            print('\nC')
            break
        elif score >= 60 and score <= 69:
            print('\nD')
            break
        elif score >= 0 and score <= 59:
            print('\nF')
            break 
        else:
            print('Input a score between 1 and 100\n')
    except ValueError:
        print('Please input a valid score\n')
