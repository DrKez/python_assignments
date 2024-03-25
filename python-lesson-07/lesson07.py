#lesson 7 vowel counter

import vowel_counting
name =  input("\033[1;35m"+"Hello! To find out how many vowels are in your name, please enter your full name: "+"\033[0m")  
print (f"My full name is {name}.")
print(f"I have a total of {len([char for char in name if char.isalpha()])} letters in my name.")
vowel_counting.characters(name)
vowel_counting.each_vowel(name)
