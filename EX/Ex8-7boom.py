# #seven_boom_ 1st version
first = 0
while first < 50:
    first += 1
    if first % 7 != 0:
        print(first)
    else:
        print("boom")
# this is the normal veersion of 7boom

# #seven_boom- 2nd version
second = 0
while second < 20:
    second += 1
    pick = input("pick a number")
    if str(pick)=="boom" and second % 7 == 0:
        print("boom")
    elif int(pick) == second and second % 7 != 0:
        print(pick)
    elif int(pick)==second and second % 7 == 0:
        print("it should have been boom")
    elif str(pick)=="boom" and second % 7 !=0:
        print("error")
    else:
        print("oh no, game over")
        break


# wrotec boom and it should be boom
# wrote boom and it shoudnt be boom
# didnt wrote boom and it should have been boom
# wrote a number and its a number