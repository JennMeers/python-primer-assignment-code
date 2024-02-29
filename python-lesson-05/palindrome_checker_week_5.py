phrase_input = input('Please enter a word or phrase:')

clean_phrase_input = phrase_input.replace(" ", "")

while not(clean_phrase_input.isalpha()):
    phrase_input = input("Please only use letters and spaces in your entry. Try again: ")
    clean_phrase_input = phrase_input.replace(" ", "")

palindrome_list = list(clean_phrase_input.lower())
palindrome_list_reverse = list(clean_phrase_input.lower())

palindrome_list_reverse.reverse()

if palindrome_list == palindrome_list_reverse:
    print(f"Your phrase '{phrase_input}' is a palindrome!")
else:
    print (f"Your phrase '{phrase_input}' is not a palindrome.")