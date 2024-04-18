
import random

def is_palindrome(user_input):
    letters = "".join(c.lower() for c in user_input if c.isalnum())
    reversed_letters = letters[::-1]
    return letters == reversed_letters

def random_words():
    with open("C:\\Data\\Python\\python_assignments\\python-lesson-10\\pd_words.txt", "r") as pd_words:
        words = pd_words.read().split('\n')
        return random.choice(words)

def random_phrases():
    with open("C:\\Data\\Python\\python_assignments\\python-lesson-10\\pd_phrases.txt", "r") as pd_phrases:
        phrases = pd_phrases.read().split('\n')
        return random.choice(phrases)
