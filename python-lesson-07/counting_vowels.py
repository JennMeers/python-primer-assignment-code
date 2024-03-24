def vowel_counting (user_name):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    vowels_in_name=0
    for item in user_name:
        if item in vowels:
            vowels_in_name += 1
    print(f"My name is {user_name}")
    if vowels_in_name == 1:
        print (f"There is {vowels_in_name} vowel in my name")
    else:
        print (f"There are {vowels_in_name} vowels in my name")