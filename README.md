# Django showcase for Haverford Digital Scholarship
This repository showcases the best practices for developing Django applications at Haverford College Digital Scholarship.


## One-time set-up steps
You'll need Python 3, pip, git, and [virtualenv](https://virtualenv.pypa.io/en/stable/) installed to run this project.

First, clone this repository with git:

```
$ git clone https://github.com/HCDigitalScholarship/django-showcase-2.git
$ cd django-showcase-2
```

(Highly recommended) Install [black](https://black.readthedocs.io/en/stable/index.html), [flake8](http://flake8.pycqa.org/en/latest/index.html#) and [pytest](https://docs.pytest.org/en/latest/index.html):

```
$ pip3 install black flake8 pytest
```

Set up the [git hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks) (only do this if you installed black and flake8 in the previous step):

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

Visit `localhost:8000` in your browser to view the site!


## Resources
- [Django's official documentation](https://github.com/HCDigitalScholarship/django-showcase-2)
- *[Test-Driven Web Development with Python](https://www.obeythetestinggoat.com/pages/book.html#toc)* by Harry J. W. Percival is a great resource for learning Django, from creating your first Django application all the way to deploying it to the public internet.
