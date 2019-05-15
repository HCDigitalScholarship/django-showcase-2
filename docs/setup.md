# One-time set-up steps
All the set-up steps should be run on your personal computer (i.e., not on the site's dev server).

You'll need Python 3, pip, git, and [virtualenv](https://virtualenv.pypa.io/en/stable/) installed to run this project.

First, you need a web driver to run the test suite. If you use Firefox, install [geckodriver](https://github.com/mozilla/geckodriver). If you use Chrome, install [chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads). This can be a bit tricky; ask a DS librarian if you need help.

Clone this repository with git and make a personal branch (`<user>` should be your Haverford username, without the brackets, e.g. `kbenston`):

```
$ git clone https://github.com/HCDigitalScholarship/django-showcase-2.git
$ cd django-showcase-2
$ git checkout -b <user>
```

(Highly recommended) Install [black](https://black.readthedocs.io/en/stable/index.html) and [flake8](http://flake8.pycqa.org/en/latest/index.html#). Note that you will need at least Python 3.6 in order to install black.

```
$ pip3 install black flake8
```

You can also install JSHint, for which you will need [npm](https://nodejs.org/en/). If you don't have npm installed on your computer already, it's probably not worth it.

```
$ npm install -g jshint
```

Set up the [git hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks) (only do this if you installed black and flake8 in the previous step):

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

Before you start developing, you'll need to change your host configuration so that the domain `dev.django-showcase.haverford.edu` and `django-showcase.haverford.edu` map to the proper IP address. Ask a DS librarian how to do this.
