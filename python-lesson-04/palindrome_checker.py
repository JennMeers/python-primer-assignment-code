word_input = (input(str('Please enter one word:')))
word_list_lower = list(word_input.lower())
word_list = word_list_lower.copy()
word_list.reverse()
print(f"Is your word '{word_input}' a palindrome? {word_list_lower == word_list}")