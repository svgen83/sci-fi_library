import json

from livereload import Server, shell

from jinja2 import Environment, FileSystemLoader, select_autoescape
from more_itertools import chunked


env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')


def rebuild():
    with open("books_description.json", "r") as file:
        books_description_json = file.read()

    books_description = json.loads(books_description_json)
    chunked_books = list(chunked(books_description, 2))
    rendered_page = template.render(books=chunked_books)
    
    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page) 
    print("Site rebuilt")






if __name__ == "__main__":  

    rebuild()
    
    server = Server()

    server.watch('template.html', rebuild)

    server.serve(root='.')

