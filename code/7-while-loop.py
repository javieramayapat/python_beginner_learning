def run():
    """
    📑Generate a program that calculates the power of two as long as it does not exceed 1000.
    """

    LIMIT = 1000
    counter = 0
    potency_2 = 2**counter
    while potency_2 < LIMIT:
        print(f"2 raised to {counter} it is equal to: {potency_2}")
        counter += 1
        potency_2 = 2**counter

    """Output 🚀
    2 raised to 0 it is equal to: 1
    2 raised to 1 it is equal to: 2
    2 raised to 2 it is equal to: 4
    2 raised to 3 it is equal to: 8
    2 raised to 4 it is equal to: 16
    2 raised to 5 it is equal to: 32
    2 raised to 6 it is equal to: 64
    2 raised to 7 it is equal to: 128
    2 raised to 8 it is equal to: 256
    2 raised to 9 it is equal to: 512
    """


if __name__ == "__main__":
    run()
