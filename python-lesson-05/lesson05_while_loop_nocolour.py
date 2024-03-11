#Lesson 5 Palindrome checker
words = input("Hi there! A palindrome is a word, phrase, sequence or number that reads the same backwards as forwards. \nPlease enter a word, phrase, sequence or number to check if it's a palindrome: ")
letters = "".join(c for c in words if c.isalnum())
letters_lower = letters.lower()
letters_list = list(letters_lower)
letters_list.reverse()
string_from_list = "".join(letters_list)
if letters_lower == string_from_list:
  print(f"  Yes, \"{words}\" is a palindrome.")
else:
  print(f"  No, \"{words}\" is not a palindrome.")

# if not a plaidome test again untill a palindrome is entered
while letters_lower != string_from_list:
   words = input("Please try another word, phrase, sequence or number: ")
   letters = "".join(c for c in words if c.isalnum())
   letters_lower = letters.lower()
   letters_list = list(letters_lower)
   letters_list.reverse()
   string_from_list = "".join(letters_list)
   if letters_lower == string_from_list:
     print(f"  Yes, \"{words}\" is a palindrome.")
   else:
     print(f"  No, \"{words}\" is not a palindrome.")

