# Similarites

Determining whether two strings are identical is (relatively!) trivial: iterate over the characters in each, checking whether each and every one is identical. But it’s non-trivial to quantify just how dissimilar two (non-identical) strings are. And it can be time-consuming, as there are multiple (and often many!) ways to transform one string into the other.

The challenge ahead is to measure the "edit distance" between two strings, the minimal number of additions, deletions, and/or edits necessary to transform one string into the other.

## How to install on your server

* You can download the zip or clone the project with git.

    `https://github.com/abdsamadf/similarities.git`

* Install `requirement.txt` via terminal:

    `pip install -r /path/to/requirements.txt`

## Running the site

* To enable all development features (including debug mode) you can export the FLASK_ENV environment variable and set it to development before running the server:

    `export FLASK_ENV=development`

* To run the application you can use the **flask** command or python’s -m switch with Flask. Before you can do that you need to tell your terminal the application to work with by exporting the **FLASK_APP** environment variable:

    `export FLASK_APP=application.py`

* To test the web app, execute

    ``` Shell
    $ flask run
        * Running on http://127.0.0.1:5000/
    ```

* Alternatively you can use python -m flask:
    ``` Shell
    $ python -m flask run
        * Running on http://127.0.0.1:5000/
    ```
