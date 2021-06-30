b = 5
import keyword
print(f'Python keywords: {keyword.kwlist}')
a = keyword.iskeyword('try')
print(a)
c = keyword.iskeyword('b')
print(c)
print(id(b))

print(type(b))
print(type(b) is int)

prog = """
import keyword
print(f'Python keywords: {keyword.kwlist}')
"""
print(prog)
exec(prog)
# # The sum of 5 and 10 is 15

x = 100
a = "x ** 2"
print(a)
print(eval(a))

b = 's'

a = {1, 2, 3}
b = {1, 2, 3}
print(hash(a))
print(hash(b))

