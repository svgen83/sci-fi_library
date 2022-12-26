import json
import os

from livereload import Server, shell

from jinja2 import Environment, FileSystemLoader, select_autoescape
from more_itertools import chunked




def rebuild():
    env = Environment(loader=FileSystemLoader('.'),
                      autoescape=select_autoescape(['html', 'xml'])
                      )
    template = env.get_template('template.html')
    os.makedirs('pages', exist_ok=True)
    
    with open("books_description.json", "r") as file:
        books_description_json = file.read()

    books_description = json.loads(books_description_json)
    books_on_pages = list(chunked(books_description, 10))


    for i, books_on_page in enumerate(books_on_pages, 1):
        row_books = list(chunked(books_on_page, 2))
        rendered_page = template.render(books=row_books)
        page_path = os.path.join('pages', f'index{i}.html')
        with open(page_path, 'w', encoding="utf8") as file:
            file.write(rendered_page) 

    print("Site rebuilt")






if __name__ == "__main__":  

    rebuild()
    
    server = Server()

    server.watch('template.html', rebuild)

    server.serve(root='.')

