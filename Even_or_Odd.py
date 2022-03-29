def Check_Even_or_Odd(x):
    if x % 2 == 0:
        return True
    else:
        return False

if __name__ == "__main__":

    x = int(input("Enter a Number to Check: "))

    Even_or_Odd = Check_Even_or_Odd(x)
    print(Even_or_Odd)

