#exercise 3 in shecode class 5
def greet(first, last, birth_year):
    age= 2021 - int(birth_year)
    print(first, last, age)
    print('Welcome', '{0},'.format(first))
    print("your initials are: ", first[0]+last[0], "and your are", age, "years old" )
greet('Shay', 'Rozner', 1996)
