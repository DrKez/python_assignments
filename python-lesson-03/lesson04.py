'''ACTIVITY DESCRIPTION
A palindrome is a word, phrase, or sequence that reads the same backwards as forwards. This activity is to write code that will check if a string is a palindrome.
Performing string manipulations like this can be a popular software developer interview or application activity.
INSTRUCTIONS
Write some code that will take an input word from a user and check if this word is a palindrome.

Steps
Ask the user for an input word and assign this to a variable
Use what we learned about lists and strings to confirm if the word is a palindrome
If the word is a palindrome, print True, otherwise, print False.


Note:
To create a list from a string
letters_in_word = list(word)
To create a string from a list, you can use the code:
list_of_letters = ["P","y","t","h","o","n"]
string_from_list = "".join(list_of_letters)
If you get stuck, try rewatching the video on List manipulation

If you need another hint:
Try converting the string into a list of strings 1 symbol long first, and then reversing the list, and then converting the list back into a string
You may want to use the methods
list.reverse()
Console.ReadLine()
Math.Pow()
int.Parse() or double.Parse()'''

input_word = input("please provide an input word")
