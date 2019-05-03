# Django showcase for Haverford Digital Scholarship
This repository showcases the best practices for developing Django applications at Haverford College Digital Scholarship.

## How to work on this repository
1. Follow the one-time set-up steps below.
2. Create a new branch named after your Haverford username: `git checkout -b <username>`.
3. Work on the repository locally, debugging using `localhost`.
4. Commit your changes and push them your personal branch on GitHub.
5. [Open a pull request](https://github.com/HCDigitalScholarship/ds-cookbook/blob/master/code_review.md) to merge into master.
6. Once your pull request has been approved and you've merged into master, follow the deployment steps in `deploy_tools/README.md`.

## One-time set-up steps
You'll need Python 3, pip, git, and [virtualenv](https://virtualenv.pypa.io/en/stable/) installed to run this project.

All the set-up steps should be run on your personal computer (i.e., not on the site's dev server).

First, clone this repository with git:

```
$ git clone https://github.com/HCDigitalScholarship/django-showcase-2.git
$ cd django-showcase-2
```

(Highly recommended) Install [black](https://black.readthedocs.io/en/stable/index.html) and [flake8](http://flake8.pycqa.org/en/latest/index.html#):

```
$ pip3 install black flake8
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

Before you start developing, you'll need to change your host configuration so that the domain `django-showcase.haverford.edu` maps to the proper IP address. Ask a DS librarian how to do this.


## Resources
- [Django's official documentation](https://github.com/HCDigitalScholarship/django-showcase-2)
- *[Test-Driven Web Development with Python](https://www.obeythetestinggoat.com/pages/book.html#toc)* by Harry J. W. Percival is a great resource for learning Django, from creating your first Django application all the way to deploying it to the public internet.
