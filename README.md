# Django showcase for Haverford Digital Scholarship
This repository showcases the best practices for developing Django applications at Haverford College Digital Scholarship.

## One-time set-up steps
You'll need Python 3, pip, git, and [virtualenv](https://virtualenv.pypa.io/en/stable/) installed to run this project. [black](https://black.readthedocs.io/en/stable/) and [flake8](https://gitlab.com/pycqa/flake8) are also highly recommended, though not strictly necessary.

First, clone this repository with git:

```
$ git clone https://github.com/HCDigitalScholarship/django-showcase-2.git
$ cd django-showcase-2
```

Set up the [git hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks):

```
$ cd .git/hooks
$ ln -s ../../githooks/pre-commit
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

## Resources
- [Django's official documentation](https://github.com/HCDigitalScholarship/django-showcase-2)
- *[Test-Driven Web Development with Python](https://www.obeythetestinggoat.com/pages/book.html#toc)* by Harry J. W. Percival is a great resource for learning Django, from creating your first Django application all the way to deploying it to the public internet.
