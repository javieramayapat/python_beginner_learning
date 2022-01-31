def run():
    # Slices's structures
    # random_string[initial character : final character : steps]

    name: str = "Francisco"

    # Ways to extract with slices from start to finish

    result = name[0:9]  # Francisco
    print(result)

    # If we are going to start at the beginning with can omit the initial character
    result = name[:9]  # Francisco
    print(result)

    # If you want to all the string from the beginning to the end you can omit values
    result = name[:]  # Francisco
    print(result)

    # Slice uses an optional third value called step

    # From the element 'start' to 'end' but skipping 2 characters
    result = name[1:6:2]
    print(result)

    # Reverse slices in slice using negative step parameter 😧
    # The functionality of this slice is to go from the end one at a time to the beginning one at a time,
    # returning any word spelled backwards.
    reverse_string = name[::-1]
    print(reverse_string)


if __name__ == "__main__":
    run()
