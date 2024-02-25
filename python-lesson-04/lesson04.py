#Lesson 4 Palindrome checker
word = input("Hi there! A palindrome is a word, phrase, or sequence that reads the same backwards as forwards.\n  Please enter a word, phrase or sequence (without punctuation) to check if its a palindrome: ")
word_letters = word.replace(" ", "")
word_lower = word_letters.lower()
letters_in_word = list(word_lower)
letters_in_word.reverse()
string_from_list = "".join(letters_in_word)
if word_lower == string_from_list:
  print(f"Yes, \"{word}\" is a palindrome.")
else:
  print(f"No, \"{word}\" is not a palindrome.")
