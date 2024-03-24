import counting_vowels
import counting_user_input

user_name = input('Please enter your name: ')
counting_vowels.vowel_counting(user_name)

user_input_letter_check = input("Would you like to check for any other letters in your name?\nPlease enter one letter to check for (input is case sensitive), or enter 'done' to exit: ")
counting_user_input.input_letter_checker(user_input_letter_check, user_name = user_name)

while len(user_input_letter_check) == 1:
   user_input_letter_check = input("Would you like to check for any other letters in your name?\nPlease enter another letter to check for, or enter 'done' to exit: ")
   counting_user_input.input_letter_checker(user_input_letter_check, user_name = user_name)