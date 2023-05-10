# Python program to check if the input number is odd or even.
# A number is even if division by 2 gives a remainder of 0.
# If the remainder is 1, it is an odd number.


def evenodd(num):
    if (num % 2) == 0:
        print("Even")
    else:
        print("Odd")


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    evenodd(num)
