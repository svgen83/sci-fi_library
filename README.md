# Сайт-библиотека научной фантастики
 
Проект представляет собой оффлайн-сайт библиотеки научной фантастики со скриптом, генерирующим страницы с книгами.
Проект является продолжением [другого проекта](https://github.com/svgen83/book_parser), созданного для парсинга страниц и скачивания книг жанра "Научная фантастика".

## Как установить

Python3 должен быть уже установлен.
Затем используйте pip (или pip3, если есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

## Как запустить
Для запуска сайта необходимо предварительно скачать книги, обложки и файл с описанием книг в формате `.json`.
О том, как это сделать, написано в описании к [упомянутому проекту](https://github.com/svgen83/book_parser).
Затем в папку, содержащую файл с описанием книг, а также каталоги с книгами и обложками следует скопировать файл `render_website.py`
Для формирования сайта из командной строки следует запустить скрипт
```
python render_website.py
```
По умолчанию программа создаст страницы, на которых будут отображаться по 10 книг, при этом файл с данными `.json` должен быть размещен в каталоге с программой.
По желанию, можно изменить настройки.
+ `-pb` или `--path_to_base` позволяют указать путь к файлу с данными;
+ `-bq` или `--books_quantity` позволяют указать желаемое количество книг на странице сайта.

Чтобы открыть сайт, необходимо перейти в каталог `pages`, который будет размещаться в папке со скриптом `render_website.py`,
а затем открыть  файл `index.html` с любым номером (например,`index1.html`) .

Сайт будет выглядеть примерно следующим образом:
![site](https://user-images.githubusercontent.com/61458549/209626259-50f36814-b698-49de-9926-af3b2c8c7b48.jpg)

Посмотреть сайт можно [тут](https://svgen83.github.io/sci-fi_library/pages/index1.html)

## Цели проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
