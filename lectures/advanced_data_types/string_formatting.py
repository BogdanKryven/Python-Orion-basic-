car = 5
print('Anna has {} cars'.format(car))

print('Anna has {1} red apple and {0} green apples'.format(5, 6))

print('Anna has {red} red apple and {green} green apples'.format(red=5, green=6))

print("Sammy has {0:4} red {1:15}!".format(5, "balloons", ))
# Sammy has    5 red balloons
#
print('A: {0:15} B: {1:15}'.format("1, 2, 3", "123456"))

name = 'Anna'
age = 25

print(f'Her name is: {name} and age: {age}')
a = 5
b = 6


def s(a, b):
    return a + b


print(f"Adding two numbers a = {a} b = {b}: {type(a)} {type(b)}")

name = "boo"
friend_name = "foo"
print('Hey %s, there is you friend %s!' % (name, friend_name))

a = 5.1
b = 6.1

print("A: %f, B: %f" % (a, b))
# 'Hey boo, there is you friend foo!'
