def is_palindrome(word: str) -> str:
    """Check if a word is a palindrome or not

    Args:
        word (str): String to be evaluated

    Returns:
        str: Return a string which specify id the word a palindrome or not
    """

    word = word.strip().replace(" ", "").lower()
    result = "It's not a Palindrome"

    if word == word[::-1]:
        result = "It's a Palindrome"

    return result


def run():
    word = input("Write your word please: ")
    print(is_palindrome(word))


if __name__ == "__main__":
    run()
