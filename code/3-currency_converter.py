def calculate_currency_exchange(type_of_coin_selected: int, amount: float) -> float:
    """Calculate the  value of one coin to dollar representation

    Args:
        type_of_coin_selected (int): type of coin
        amount (float): amount of money in the value of this currency

    Returns:
        float: Value equivalent in dollars
    """

    result: float = 0

    if type_of_coin_selected == 1:
        result = amount / 20.47
        result = round(result, 2)
    elif type_of_coin_selected == 2:
        result = amount / 104.30
        result = round(result, 2)
    elif type_of_coin_selected == 3:
        result = amount / 3956.44
        result = round(result, 2)
    else:
        raise ("Your selected option is not valid")

    return result


def run():

    currency_converter_menu: str = """

    *********** Welcome to currency converter ***********

    Please select type currency converter:

    [1] Mexican peso to US Dollar
    [2] Argentine Peso to US Dollar
    [3] Colombian Peso to US Dollar

    *****************************************************

    """

    print(currency_converter_menu)
    type_of_coin_selected: int = int(input("Type your selected option: "))
    amount: float = float(input("Amount of money to convert: "))
    result = calculate_currency_exchange(
        type_of_coin_selected=type_of_coin_selected, amount=amount
    )
    print("You have: " + "$" + str(result) + " Dollars")


if __name__ == "__main__":
    run()
