def run():
    # Logical operators

    # and -> It works to compare whether two values are true
    is_student: bool = True
    print('is student has a value:' + str(is_student))

    is_working: bool = False
    result = is_student and is_working
    print('the result of is: ' + str(result))

    # or -> It works to compare if at least one of the two values is false
    is_programmer: bool = False
    result = is_student or is_programmer
    print('the result of is: ' + str(result))

    # comparison operators

    # values to compare
    number1: int = 5
    number2: int = 5
    number3: int = 7

    # [==] [Equal]-> It compares two values and tells you if they are equal or not.
    result = number1 == number2
    print(str(number1) + ' is equal to ' + str(number2) + ': ' + str(result))

    # [!=] [Distinct] -> It compares two values and tells you if they are different or not.
    result = number1 != number3
    print(str(number1) + ' is distinct to ' +
          str(number3) + ': ' + str(result))

    # [>] [Greater than] -> It compare if one value is greater than other
    result = number3 > number2
    print(str(number3) + ' is greater than ' +
          str(number2) + ': ' + str(result))

    # [<] [Less than] -> It compare if one value is less than other
    result = number1 < number3
    print(str(number1) + ' is less than ' + str(number3) + ': ' + str(result))

    # [>=] [Greater or equal than] -> It compare if one value is greater than other
    result = number3 >= number2
    print(str(number3) + ' greater or equal than ' +
          str(number2) + ': ' + str(result))

    # [<=] [Less or equal than] -> It compare if one value is greater than other
    result = number1 <= number2
    print(str(number1) + ' less or equal than ' +
          str(number2) + ': ' + str(result))


if __name__ == "__main__":
    run()
