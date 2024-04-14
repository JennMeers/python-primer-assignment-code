import tkinter as tk

class PalindromeApp:
    def __init__ (self, root):
        self.root =  root
        root.title("Palindrome checker")
        root.geometry("400x200")
        label = tk.Label(root, text = "Please enter your word ")
        label.grid(row = 0, column = 0)
        entry = tk.Entry(root)
        entry.grid(row = 0, column = 1)


    def palindrome_app(self, entry):
        input_palindrome = entry.get()
        clean_phrase_input = input_palindrome.replace(" ", "")
        while not(clean_phrase_input.isalpha()):
            phrase_input = input("Please only use letters and spaces in your entry. Try again: ")
            clean_phrase_input = phrase_input.replace(" ", "")
        palindrome_list = list(clean_phrase_input.lower())
        palindrome_list_reverse = list(clean_phrase_input.lower())
        palindrome_list_reverse.reverse()
        if palindrome_list == palindrome_list_reverse:
            print(f"Your phrase '{input_palindrome}' is a palindrome!")
        else:
            print(f"Your phrase '{input_palindrome}' is not a palindrome.")

        self.root.mainloop()