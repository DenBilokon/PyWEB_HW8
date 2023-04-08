import json

from models import Author, Quotes


def load_authors(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        authors_data = json.load(file)

    for i in authors_data:
        person = Author(fullname=i.get('fullname'),
                        born_date=i.get('born_date'),
                        born_location=i.get('born_location'),
                        description=i.get('description'))
        person.save()


def load_quotes(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        quotes_data = json.load(file)

    for q in quotes_data:
        author = Author.objects(fullname=q.get("author", None))
        new_quote = Quotes(tags=q.get('tags'),
                           quote=q.get('quote', None),
                           author=author[0])
        new_quote.save()


if __name__ == '__main__':
    load_authors('authors.json')
    load_quotes('quotes.json')

