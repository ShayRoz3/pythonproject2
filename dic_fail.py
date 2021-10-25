x = {"class": "mathh", "name": "jhon", "age": "34"}
print(x)
x.update({"class": "math"})
print(x)
new_x = x, {"class":("math", "biology"), "name": "nathan"}
print(new_x)
#i cant update the dictionary dfor some reson

m = {"a": 2, "b": 4, "c":3}
print(m)
m.update(a=5, b="math")
print(m)
m.update(a=(4, 7), c="no no", g="bio" )
print(m)
#successs