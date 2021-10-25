import struct
dir()   # show the names in the module namespace
['__builtins__', '__doc__', '__name__', 'struct']
dir(struct)   # show the names in the struct module
['Struct', '__builtins__', '__doc__', '__file__', '__name__',
 '__package__', '_clearcache', 'calcsize', 'error', 'pack', 'pack_into',
 'unpack', 'unpack_from']
class Shape(object):
        def __dir__(self):
            return ['area', 'perimeter', 'location']
s = Shape()
dir(s)
['area', 'perimeter', 'location']
print(dir(s))


#function11
def middle_way(a, b):
  print([a[1], b[1]])

middle_way([1, 2, 3], [4, 5, 6])
middle_way([7, 7, 7], [3, 8, 0])
middle_way([5, 2, 9], [1, 4, 5])

