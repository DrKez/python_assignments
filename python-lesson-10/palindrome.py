
def palindrome(user_input):
    letters = "".join(c.lower() for c in user_input if c.isalnum())
    reversed_letters = letters[::-1]

    if letters == reversed_letters:
        print("\033[1;32m" + f"Yes, \"{user_input}\" is a palindrome." + "\033[37m")
    else:
        print("\033[1;31m" + f"No, \"{user_input}\" is not a palindrome.")

