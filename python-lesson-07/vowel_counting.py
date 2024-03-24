
name = "hello"

def characters(name):
    count = {'vowels': 0, 'consonants': 0}
    for char in name:
        if char.lower() in 'aeiou':
            count['vowels'] += 1
        elif char.isalpha():
            count['consonants'] += 1
    print("I have {vowels} vowels in my name and {consonants} constanants.".format(**count))

#for vowels only
def vowels(name):
    vowels = len([char for char in name if char.lower() in {'a', 'e', 'i', 'o', 'u'}])
    print(f"I have {vowels} vowels in my name.")    

#for constants only
def consonants(name):
    consonants = len([char for char in name if char.isalpha() and char.lower() not in {'a', 'e', 'i', 'o', 'u'}])
    print(f"I have {consonants} consonants in my name.")
