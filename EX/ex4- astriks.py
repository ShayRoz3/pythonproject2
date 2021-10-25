def star_girl():
    for i in range(6):
        print(i * "*")
star_girl()
# #completed\\
print(" ")
def star_boy():
    for i in range(3):
        i = "***" + i * "*"
        print(i)
star_boy()
# completed
# i >= 3:
#             print(i * "* - *")
# * - ** - ** - ** - *
# * - ** - ** - ** - ** - *
def star_kids():
    i = "*"
    for i in range(6):
        if i <= 3:
            print(i * "*")
        else:
            print((i - 4) * "*" )
star_kids()

# not completed