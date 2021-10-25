def some_info():
    return 'What is your given name? '
first = input(some_info())
def last_name():
    return 'What is your surname name? '
last = input(last_name())
def birth_year():
    return 'When were you born? '
age = input(birth_year())
new_age = 2021 - int(age)

print(first)
print(last)
print(new_age)
print('Your initials are ', first[0]+last[0], ' and you are ', str(new_age), ' years old')
print("Thank you for playing")

#
# #SOLOTION SHE CODE

def greetings(first, last, age):
    birth = 2021- age
    print("welcome, your initials are " + first[0] + last[0] + " and you are " + str(birth) + " years old")

greetings("Shay", "Roz", 1996)
# my kind of functions


# exercise 3 in shecode class 5
def greet(first, last, birth_year):
    age = 2021 - int(birth_year)
    print(first, last, age)
    print('Welcome', '{0},'.format(first))
    print("your initials are: ", first[0] + last[0], "and your are", age, "years old")

greet('Shay', 'Rozner', 1996)
