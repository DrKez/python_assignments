import tkinter as tk
import palindrome as pd
import random

class Root(tk.Tk):

    def __init__(self):
        super().__init__()
        self.configure(bg='#FCE38A')
        self.geometry('800x600')
        self.title('Palindrome RadaR')

        self.label_0 = tk.Label(self, text="\nHi there!\nWelcome to Palindrome RadaR:\nAn app that will check if your text is a palindrome.\n\nA palindrome is a word, phrase, sequence, or number\nthat reads the same backwards as forwards.", font='Helvetica 14 bold', fg='#4793AF', bg='#FCE38A')
        self.label_0.pack()
        self.label_1 = tk.Label(self, text="\nPlease enter a word, phrase, sequence, or number\nto check if it's a palindrome:", font='Helvetica 16 bold', fg='#8B322C', bg='#FCE38A')
        self.label_1.pack()

        self.entry_0 = tk.Entry(self, width=80, font='Helvetica 12')
        self.entry_0.pack()
        self.btn = tk.Button(self, text='Enter', font='Helvetica 12', command=self.submit)
        self.btn.pack(pady=10)        
        self.label_2 = tk.Label(self, fg='#8B322C', bg='#FCE38A')
        self.label_2.pack()

        self.label_3 = tk.Label(self, text="\nClick below for examples of Palindrome words:", font='Helvetica 16 bold', fg='#8B322C', bg='#FCE38A')
        self.label_3.pack()
        self.btn_0 = tk.Button(self, text='Palindrome Words', font='Helvetica 12', command=self.rand_words)
        self.btn_0.pack(pady=10)

        self.label_4 = tk.Label(self, text="\nClick below for examples of Palindrome phrases:", font='Helvetica 16 bold', fg='#8B322C', bg='#FCE38A')
        self.label_4.pack()
        self.btn_1 = tk.Button(self, text='Palindrome Phrases', font='Helvetica 12', command=self.rand_phrases)
        self.btn_1.pack(pady=10)

    def submit(self):
        user_input = self.entry_0.get().strip()
        if user_input:
            if pd.is_palindrome(user_input):
                self.label_2.config(text=f"Yes, \"{user_input}\" is a palindrome.",font='Helvetica 12 bold', fg='#1B9A59')
            else: 
                self.label_2.config(text=f"No, \"{user_input}\" is not a palindrome.",font='Helvetica 12 bold', fg='#C21807')
        else:
            self.label_2.config(text="Please enter something!",font='Helvetica 12 bold', fg='#C21807')

    def rand_words(self):
        rand_words = tk.Toplevel(self)
        rand_words.title("Random Palindromes Words")
        rand_words.geometry("1200x1200")
        rand_words.configure(bg='#E1F7F5')
        rand_words.btn = tk.Button(rand_words, text='Click to generate random palindrome words', command=lambda: self.gen_word(rand_words), font='Helvetica 12 bold', bg='#DD5746')
        rand_words.btn.pack(pady=10)
        
    def gen_word(self, rand_words):
        rand_words.label_5 = tk.Label(rand_words, text=pd.random_words(), fg='#1B9A59', font='Helvetica 12 bold', bg='#E1F7F5')
        rand_words.label_5.pack()
        x = random.randrange(1000)
        y = random.randrange(500)
        rand_words.label_5.place(x=x, y=y)
        
    def rand_phrases(self):
        rand_phrases = tk.Toplevel(self)
        rand_phrases.title("Random Palindromes Phrases")
        rand_phrases.geometry("1200x1200")
        rand_phrases.configure(bg='#9AC8CD')
        rand_phrases.btn = tk.Button(rand_phrases, text='Click to generate random palindrome phrases', command=lambda: self.gen_phrase(rand_phrases), font='Helvetica 12 bold', bg='#F08A5D')
        rand_phrases.btn.pack(pady=10)

    def gen_phrase(self, rand_phrases):
        rand_phrases.label_6 = tk.Label(rand_phrases, text=pd.random_phrases(), fg='#393E46', font='Helvetica 12 bold', bg='#9AC8CD')
        rand_phrases.label_6.pack()
        x = random.randrange(800)
        y = random.randrange(800)
        rand_phrases.label_6.place(x=x, y=y)

window = Root()
window.mainloop()