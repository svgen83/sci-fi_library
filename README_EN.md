# Science Fiction Library Site
 
The project is an offline science fiction library site with a script that generates book pages.
The project is a continuation of [another project](https://github.com/svgen83/book_parser) created to parse pages and download science fiction books.

## How to install

Python3 should already be installed.
Then use pip (or pip3 if there is a conflict with Python2) to install the dependencies:
```
pip install -r requirements.txt
```

## How to start
To launch the site, you must first download books, covers and a file with a description of books in the `.json` format.
How to do this is written in the description of the [mentioned project] (https://github.com/svgen83/book_parser).
Then copy the file `render_website.py` to the folder containing the file with the description of the books, as well as directories with books and covers
To create a site from the command line, run the script
```
python render_website.py
```
By default, the program will create pages on which 10 books will be displayed, while the `.json` data file must be placed in the directory with the program.
You can change the settings if you wish.
+ `-pb` or `--path_to_base` allow you to specify the path to the data file;
+ `-bq` or `--books_quantity` allows you to specify the desired number of books on the site page.

To open the site, you need to go to the `pages` directory, which will be located in the folder with the `render_website.py` script,
and then open the `index.html` file with any number (eg `index1.html`) .

The site will look something like this:
![site](https://user-images.githubusercontent.com/61458549/209626259-50f36814-b698-49de-9926-af3b2c8c7b48.jpg)

You can view the site [here](https://svgen83.github.io/sci-fi_library/pages/index1.html)

## Project Goals

The code was written for educational purposes in an online course for web developers [dvmn.org](https://dvmn.org/).
