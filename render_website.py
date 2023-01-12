import argparse
import json
import logging
import os

from jinja2 import Environment, FileSystemLoader, select_autoescape
from livereload import Server
from math import ceil
from more_itertools import chunked


def parse_cmd():
    parser = argparse.ArgumentParser(description='''
    Программа для формирования сайта библиотеки''')

    parser.add_argument(
        '-pb', dest='path_to_base',
        type=str, default='books_description.json',
        help='путь к файлу с описанием книг')

    parser.add_argument(
        '-bq', dest='books_quantity',
        type=int, default=10,
        help='количество книг на странице')

    return parser.parse_args()


def rebuild():
    args = parse_cmd()
    in_row_quantity = 2

    env = Environment(loader=FileSystemLoader('.'),
                      autoescape=select_autoescape(['html', 'xml'])
                      )
    template = env.get_template('template.html')
    os.makedirs('pages', exist_ok=True)

    with open(args.path_to_base) as file:
        books_descriptions = json.load(file)

    for book_descriptions in books_descriptions:
        image_url = book_descriptions['image_path'].replace('\\', '/')
        book_url = book_descriptions['text_path'].replace('\\', '/')
        genres = book_descriptions['genres'].split('\n')
        book_descriptions.update({'image_url': image_url,
                                  'book_url': book_url,
                                  'genres': genres})

    books_on_pages = list(chunked(books_descriptions, args.books_quantity))
    page_quantity = ceil(len(books_descriptions)/args.books_quantity)
    page_numbers = list(range(1, page_quantity + 1))

    for current_page, books_on_page in enumerate(books_on_pages, 1):
        row_books = list(chunked(books_on_page, in_row_quantity))
        rendered_page = template.render(books=row_books,
                                        pages=page_numbers,
                                        current_page=current_page,
                                        last_page=page_quantity
                                        )
        page_path = os.path.join('pages', f'index{current_page}.html')
        with open(page_path, 'w', encoding='utf8') as file:
            file.write(rendered_page)


def main():

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    rebuild()
    logger.info('Site rebuilt')

    server = Server()
    server.watch('template.html', rebuild)
    server.serve(root='.')


if __name__ == '__main__':
    main()
