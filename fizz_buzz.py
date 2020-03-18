# Fizz_Buzz function.
def fizz_buzz(input):
    if input % 15 == 0:
        return "Fizz_Buzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input


print(fizz_buzz(30))

# 2. Another Fizz_Buzz function.


def fizzbuzz():
    user = int(input("Choose your number from 1 to 100: "))
    if user % 15 == 0:
        return "FizzBuzz"
    if user % 3 == 0:
        return "Fizz"
    if user % 5 == 0:
        return "Buzz"


print(fizzbuzz())
