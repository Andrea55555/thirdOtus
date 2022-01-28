import csv
import json

result = {'users': []}

with open("../../../3/thirdOtus/files/users.json", "r") as f:
    users = json.loads(f.read())


def read_users():
    for user in users:
        result.get('users').append({'name': user['name'], 'gender': user['gender'], 'address': user['address'],
                                    'age': user['age'], 'books': []})


def read_books():
    books_read = []
    with open('../../../3/thirdOtus/files/books.csv', newline='') as f:
        for book_one in csv.DictReader(f):
            books_read.append(
                {'title': book_one['Title'], 'author': book_one['Author'], 'pages': int(book_one['Pages']),
                 'genre': book_one['Genre']})
    return books_read


read_users()
books = read_books()
x = 0

for i in range(0, len(books)):
    a = i
    if i >= len(result.get('users')):
        if i % len(result.get('users')) == 0:
            x += 1
        a = i - ((len(result.get('users'))) * x)
    u = result.get('users')[a].get('books').append(books[i])

with open('../../../3/thirdOtus/code/data.json', 'w') as f:
    json.dump(result['users'], f)