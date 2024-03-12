#Lesson 5 Palindrome checker

print("\033[1m"+"Hi there! A palindrome is a word, phrase, sequence or number that reads the same backwards as forwards.")
has_palindrome = False
 
while not has_palindrome:
   words = input("\033[0m"+"Please enter a word, phrase, sequence or number to check if it's a palindrome: ")
   letters = "".join(c for c in words if c.isalnum())
   letters = "".join(c for c in words if c.isalnum())
   letters_lower = letters.lower()
   letters_list = list(letters_lower)
   letters_list.reverse()
   string_from_list = "".join(letters_list)
   if letters_lower == string_from_list:
    has_palindrome = True
    print("\033[1;32m"+f"  Yes, \"{words}\" is a palindrome."+"\033[37m")
   else:
    print("\033[1;31m"+f"  No, \"{words}\" is not a palindrome.")
    continue

