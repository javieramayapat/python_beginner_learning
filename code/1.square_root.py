import math

# Exercise: Create a program that calculates the square root given a number entered by the user.


def get_square(number: int) -> int:
    """Function to get the square by a number give by the user

    Args:
        number (int): number to calculate the square root

    Returns:
        int: square root of the number
    """
    return math.sqrt(number)


def run():
    try:
        number = int(input("Please insert the number to calculate its square: "))
        result = get_square(number)
        print(result)
    except ValueError:
        raise ValueError("String can´t be  changed into integer")


if __name__ == "__main__":
    run()
