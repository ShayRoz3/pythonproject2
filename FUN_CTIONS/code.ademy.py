def shout(phrase):
  if phrase == phrase.upper():
    return "YOU'RE SHOUTING!"
  else:
    return "can you speak up?"
print(shout('im ok'))
print(shout('I DONT WANT TO'))

def cube(num):
    return num**3, num*num*num
print(cube(2))


def distance_from_zero(num):
    if type(num) == int or type(num) == float:
        return abs(num)
    else:
        return "nope"
distance_from_zero(5)

