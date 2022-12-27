import json
import logging
import os

from jinja2 import Environment, FileSystemLoader, select_autoescape
from livereload import Server
from math import ceil
from more_itertools import chunked


logger = logging.getLogger(__name__)


def rebuild():
    on_page_quantity = 10
    in_row_quantity = 2

    env = Environment(loader=FileSystemLoader('.'),
                      autoescape=select_autoescape(['html', 'xml'])
                      )
    template = env.get_template('template.html')
    os.makedirs('pages', exist_ok=True)

    with open("books_description.json", "r") as file:
        books_description_json = file.read()

    books_description = json.loads(books_description_json)

    books_on_pages = list(chunked(books_description, on_page_quantity))

    page_quantity = ceil(len(books_description)/len(books_on_pages))
    page_numbers = list(range(1, page_quantity + 1))

    for current_page, books_on_page in enumerate(books_on_pages, 1):
        row_books = list(chunked(books_on_page, in_row_quantity))
        rendered_page = template.render(books=row_books,
                                        pages=page_numbers,
                                        current_page=current_page,
                                        last_page=page_quantity
                                        )
        page_path = os.path.join('pages', f'index{current_page}.html')
        with open(page_path, 'w', encoding="utf8") as file:
            file.write(rendered_page)

    logger.info("Site rebuilt")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    rebuild()

    server = Server()
    server.watch('template.html', rebuild)
    server.serve(root='.')
