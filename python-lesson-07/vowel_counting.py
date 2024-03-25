name = "hello"

def characters(name):
    count = {'vowels': 0, 'consonants': 0}
    for char in name:
        if char.lower() in 'aeiou':
            count['vowels'] += 1
        elif char.isalpha():
            count['consonants'] += 1
    print("I have {vowels} vowels and {consonants} constanants in my name.".format(**count))

#for vowels only
def vowels(name):
    vowels = len([char for char in name if char.lower() in {'a', 'e', 'i', 'o', 'u'}])
    print(f"I have {vowels} vowels in my name.")    

#for constants only
def consonants(name):
    consonants = len([char for char in name if char.isalpha() and char.lower() not in {'a', 'e', 'i', 'o', 'u'}])
    print(f"I have {consonants} consonants in my name.")

#count of each vowel
def each_vowel(name):
    a = len([char for char in name if char.lower() in {'a'}])
    e = len([char for char in name if char.lower() in {'e'}])
    i = len([char for char in name if char.lower() in {'i'}])
    o = len([char for char in name if char.lower() in {'o'}])
    u = len([char for char in name if char.lower() in {'u'}])
    print(f"I have the following number of each vowel in my name: \n a:{a}, e:{e}, i:{i}, o:{o}, u:{u}" )

