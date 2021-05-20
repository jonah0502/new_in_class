def askForInt():
    while True:
        try:
            result = int(input("Please provide a year: "))
        except:
            print("Hey, that is not a number!!")
            continue
        else:
            break
    return result

def isLY(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
