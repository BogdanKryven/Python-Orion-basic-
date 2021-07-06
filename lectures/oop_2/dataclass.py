import dataclasses

@dataclasses.dataclass
class Article:
    topic: str
    contributor: str
    language: str
    author: str
    page: int

class Info:
    name: str
    surname: str

article = Article('OOP lecture 2', 'Rostyslav Kitsylinksyy', 'EN', 'Rostyslav', '17')
article_1 = Article('OOP lecture 3', 'Rostyslav Kitsylinksyy', 'EN', 'Rostyslav', 27)

article_dict = {'topic': 'OOP lecture 2',
                'contributor': 'Rostyslav Kitsylinksyy',
                'language': 'EN',
                'author': 'Rostyslav',
                'page': 17}

print(article)
article.page = 25
print(article.page)
print(article.author)
print(article_1.topic)
print(article_dict['topic'])


@dataclasses.dataclass(frozen=True)
class Book:
    title: str
    author: str

book = Book('Kobzar', 'Shevchenko')
book_1 = Book('Лісова Пісня', 'Леся Українка')

books = (book, book_1)

for b in books:
    print(f'I read this book last year: {b.author}, {b.title}')