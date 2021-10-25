import string
string.ascii_lowercase
# print(a)
a = list(string.ascii_lowercase)
b = list(string.ascii_uppercase)
loopi = {}
for i in a:
    if i < "n":
        loopi[i] = chr(ord(i) + 13)
    else:
        loopi[i] = chr(ord(i) - 13)
for i in b:
    if i < "N":
        loopi[i] = chr(ord(i) + 13)
    else:
        loopi[i] = chr(ord(i) - 13)
loopi["!"] = "!"
loopi[" "] = " "
loopi["'"] = "'"
loopi["."] = "."
loopi[","] = ","
# print(loopi)

def super_encode(massage, loopi):
    d = loopi
    new_str = ""
    for char in massage:
            new_str = new_str + d[char]
    print(new_str)

super_encode("V NZ YRNEAVAT CLGUBA JVGU FUR PBQRF NPNQRZL!", loopi)
super_encode("komo estas amigo", loopi)
super_encode("tbbq yhpx", loopi)
super_encode("thankss", loopi)
super_encode("Lbh'er irel jrypbzr!", loopi) #You're very welcome
