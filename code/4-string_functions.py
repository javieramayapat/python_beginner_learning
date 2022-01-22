def run():
    name = "javier amaya patricio "
    print(name)

    # upper() -> Return a copy of the string converted to uppercase.
    name = name.upper()
    print(name)

    # lower() -> Return a copy of the string converted to lowercase
    name = name.lower()
    print(name)

    # capitalize() -> Transform the first letter of each word to upper case
    name = name.capitalize()
    print(name)

    # strip() -> Return a copy of the string with leading and trailing whitespace removed.
    name = name.strip()
    print(name)

    # replace() -> Return a copy with all occurrences of substring old replaced by new.
    name = name.replace('o', 'u')
    print(name)

    # indexes[0] -> We can access to the characters of my string and play with them
    print(name[0])
    print(name[1])
    print(name[3])
    print(name[8])
    print(name[4])

    # len(string) -> Allow me to know the length of a string
    length = len(name)
    print(length)


if __name__ == "__main__":
    run()
