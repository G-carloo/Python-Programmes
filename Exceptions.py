from math import sqrt
def sqrt_of_sum(number_1, number_2):
    """
    >>> number_1 = 2

    >>> number_2 = 2

    >>> sqrt_of_sum(number_1, number_2)
    2.0
    """
    return sqrt(number_1 + number_2)

try:
    number_1 = int(input("Please enter your first number:\n"))
    number_2 = int(input("Please enter your second number:\n"))

except TypeError:
    print("TypeError Occured:\n")

except KeyboardInterrupt:
    print("KeyboardError Occured:\n")

except ValueError:
    print("ValueError Occured:\n")


else:
    print(sqrt_of_sum(number_1, number_2))