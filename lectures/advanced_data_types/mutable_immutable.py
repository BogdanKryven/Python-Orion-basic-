# list
lst = [1, "2", ['sd',1, {'key': ''}]]
lst1 = [1, 2, 3]

# dict
dct = {"key": "value"}
dct1 = {"name": 'Rostyslav'}
name = dct1['name']

# set
st = {'1', '2', '3'}

# bytearray
# bytearray() method returns a bytearray
# object which is an array of given bytes.
# It gives a mutable sequence of
# integers in the range 0 <= x < 256.
#bytearray(source, encoding, errors)
# simple list of integers
list = [1, 2, 3, 4]
# iterable as source
array = bytearray(list)
print(array)
# bytearray(b'\x01\x02\x03\x04')
print("Count of bytes:", len(array))
# Count of bytes: 4

# user-defined classes

# int
i = 1
# float
flt = 1.1
# complex
cmplx = complex(2, -3)
# z = (2-3j)
# bool
bl = True
# string
strng = 'str'
# tuple
tpl = (1, 2, 3)
# range
rng = range(3, 6)

# frozenset
# tuple of numbers
nu = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# converting tuple to frozenset
fnum = frozenset(nu)
# frozenset({1, 2, 3, 4, 5, 6, 7, 8, 9})

# bytes
x = bytes(4)
# x = b'\x00\x00\x00\x00'