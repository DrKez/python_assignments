#Lesson 5 Palindrome checker
words = input("Hi there! A palindrome is a word, phrase, or sequence that reads the same backwards as forwards.\n  Please enter a word, phrase or sequence to check if it's a palindrome: ")
letters = "".join(c for c in words if c.isalpha())
letters_lower = letters.lower()
letters_list = list(letters_lower)
letters_list.reverse()
string_from_list = "".join(letters_list)
if letters_lower == string_from_list:
  print(f"Yes, \"{words}\" is a palindrome.")
else:
  print(f"No, \"{words}\" is not a palindrome.")
repeat = input("would u like to test another? plesea type yes or no")
#while repeat = "yes"