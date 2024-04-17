import tkinter as tk
import palindrome as pd

class Root(tk.Tk):

    def __init__(self):
        super().__init__()
        self.configure(bg='#FFC470')
        self.geometry('650x350')
        self.title('Palindrome RadaR')
        self.label_0 = tk.Label(self, text="\nHi there!\nWelcome to Palindrome RadaR:\nAn app that will check if your text is a palindrome.\n\nA palindrome is a word, phrase, sequence, or number\nthat reads the same backwards as forwards.", font='Helvetica 14 bold', fg='#4793AF', bg='#FFC470')
        self.label_0.pack()
        self.label_1 = tk.Label(self, text="\nPlease enter a word, phrase, sequence, or number\nto check if it's a palindrome:", font='Helvetica 16 bold', fg='#8B322C', bg='#FFC470')
        self.label_1.pack()
        self.entry_0 = tk.Entry(self, width=100)
        self.entry_0.pack()
        self.btn = tk.Button(self, text='Enter', command=self.submit)
        self.btn.pack(pady=10)
        self.label_2 = tk.Label(self, font='Helvetica 16 bold', fg='#8B322C', bg='#FFC470')
        self.label_2.pack()

    def submit(self):
        user_input = self.entry_0.get()
        letters = "".join(c.lower() for c in user_input if c.isalnum())
        reversed_letters = letters[::-1]
        if letters == reversed_letters:
            self.label_2.config(text=f"Yes, \"{user_input}\" is a palindrome.", fg='#1B9A59')
        else:
            self.label_2.config(text=f"No, \"{user_input}\" is not a palindrome.", fg='#C21807')

    #def submit(self):
        #pd.palindrome(user_input=self.entry_0.get())
        #if pd.palindrome.letters == pd.palindrome.reversed_letters:
            #self.label_2['text'] = (f"Yes, \"{user_input}\" is a palindrome.")
            #else:
            #self.label_2['text']= (f"No, \"{user_input}\" is not a palindrome.")
              

window = Root()
window.mainloop()
