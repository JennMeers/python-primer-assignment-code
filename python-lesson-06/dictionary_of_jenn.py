about_user = {}
user_name = input("Hi, please enter your name: ")
about_user['name'] = user_name

my_name= ('Jenn')
about_me = {'name': (my_name), 
            'age': '31', 
            'hobby': 'hiking', 
            'favourite colour': 'yellow', 
            'favourite animal': 'bats'}
print(f"Hi {user_name}")
for key, value in about_me.items():
    print(f"My {key} is {value}")

print("I wonder if we have anything in common...")
user_age =  input("What is your age? (Please use full numbers only): ")
about_user['age'] = user_age
user_hobby =  input("What is your hobby? ")
about_user['hobby'] = user_hobby.lower()
user_favourite_colour =  input("What is your favourite colour? ")
about_user['favourite colour'] = user_favourite_colour.lower()
user_favourite_animal =  input("What is your favourite animal? ")
about_user['favourite animal'] = user_favourite_animal.lower()
 
about_me_set = set(about_me.values())
about_user_set = set(about_user.values())

similar_interests = about_me_set & about_user_set
for key in similar_interests:
    print(f"You and I have {key} in common in our lists")

if (len(similar_interests) == 0):
    print("Looks like you and I don't have anything in common on our lists today")