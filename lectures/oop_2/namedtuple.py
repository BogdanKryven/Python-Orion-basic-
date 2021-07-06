from collections import namedtuple

Author = namedtuple('Author', ['topic', 'name', 'language'])

author_1 = Author('OOP part 2', 'Rostyslav', 'EN')

print(author_1[0])
print(author_1.topic)