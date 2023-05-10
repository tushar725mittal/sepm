def PrimeChecker(a):
    # Checking that given number is more than 1
    if a > 1:
        # Iterating over the given number with for loop
        for j in range(2, int(a / 2) + 1):
            # If the given number is divisible or not
            if (a % j) == 0:
                print("Non-Prime")
                break
        # Else it is a prime number
        else:
            print("Prime")
    # If the given number is 1
    else:
        print(a, "is not a prime number")


if __name__ == "__main__":
    # Taking an input number from the user
    a = int(input("Non-Prime"))
    # Printing result
    PrimeChecker(a)
