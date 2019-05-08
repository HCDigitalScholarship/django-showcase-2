# One-time set-up steps
All the set-up steps should be run on your personal computer (i.e., not on the site's dev server).

You'll need Python 3, pip, git, and [virtualenv](https://virtualenv.pypa.io/en/stable/) installed to run this project.

You need a web driver to run the test suite. If you use Firefox, install [geckodriver](https://github.com/mozilla/geckodriver). If you use Chrome, install [chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads).

First, clone this repository with git:

```
$ git clone https://github.com/HCDigitalScholarship/django-showcase-2.git
$ cd django-showcase-2
```

(Highly recommended) Install [black](https://black.readthedocs.io/en/stable/index.html), [flake8](http://flake8.pycqa.org/en/latest/index.html#) and [JSHint](https://jshint.com/). Note that you will need at least Python 3.6 in order to install black, and you will need [npm](https://nodejs.org/en/) to install JSHint.

```
$ pip3 install black flake8
$ npm install -g jshint
```

Set up the [git hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks) (only do this if you installed the programs in the previous step):

```
$ cd .git/hooks
$ ln -s ../../githooks/pre-commit
$ cd ../..
```

Next, create a new virtual environment and activate it:

```
$ virtualenv .venv --python=python3
$ source .venv/bin/activate
```

Install the project requirements:

```
$ pip3 install -r requirements.txt
```

Apply migrations to the database:

```
$ ./manage.py migrate
```

Now you should be able to run the server:

```
$ ./manage.py runserver
```

Visit `localhost:8000` in your browser to view the site!

Before you start developing, you'll need to change your host configuration so that the domain `django-showcase.haverford.edu` maps to the proper IP address. Ask a DS librarian how to do this.
