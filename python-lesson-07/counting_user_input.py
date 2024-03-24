def input_letter_checker (user_input_letter_check, user_name):
    user_input_letter_count = 0
    for input in user_input_letter_check:
        if user_input_letter_check == 'done':
            break
        else:
            list(user_name)
            for item in user_name:
                if item in user_input_letter_check:
                      user_input_letter_count += 1
            if user_input_letter_count == 1:
                print (f"There is {user_input_letter_count} {user_input_letter_check} in my name")
            else:
                print (f"There are {user_input_letter_count} {user_input_letter_check}'s in my name")