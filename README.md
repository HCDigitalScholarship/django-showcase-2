# Django showcase for Haverford Digital Scholarship
This repository showcases the best practices for developing Django applications at Haverford College Digital Scholarship.


## How to start
1. Read this readme and browse the source code, which is mostly well-commented, to get acquainted with the project.
2. Read the one-time set-up steps in `docs/setup.md`.
3. Read the workflow steps in `docs/workflow.md`
4. Read the deployment steps in `docs/deployment.md`.


## Organization
### Django apps and files
- `interns/`: An app for the interns page. See `docs/interns.md` for details.
- `justhtml/`: An app that serves all the static HTML of the site that isn't otherwise associated with an app. The code in this app has especially detailed comments, so check it out first if you're new to Django.
- `showcase_site/`: The site directory, containing the settings file and other site-wide configuration files.
- `tablebuilder/`: An app for a simple JavaScript page.
- `textviewer/`: An app for a text-viewer web application that demonstrates the use of database models.
- `manage.py`: Django's management script.

### Other directories and files
- `deploy_tools/`: Scripts and config files for deploying the site to a remote server
- `docs/`: Documentation for the project.
- `githooks/`: The project's [git hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks)
- `logs/`: An empty directory for logs. Django will complain if it doesn't exist.
- `test/`: The site's functional tests. Note that the unit tests are contained in the `tests.py` modules of each individual app.
- `.flake8`: Configuration for [flake8](http://flake8.pycqa.org/en/latest/index.html#).
- `.gitignore`: The list of files to be ignored by git.
- `.jshintrc`: Configuration for [JSHint](https://jshint.com/).
- `.travis.yml`: Configuration for [Travis](https://travis-ci.com/).
- `README.md`: This file!
- `deploy`: The one-step deployment script. See `docs/deployment.md` for details.
- `requirements.txt`: The list of required Python packages.
- `test_local`: The script for running the test suite against a local server.
- `test_staging`: The script for running the test suite against the staging server.


## Resources
- [Django's official documentation](https://github.com/HCDigitalScholarship/django-showcase-2)
- *[Test-Driven Web Development with Python](https://www.obeythetestinggoat.com/pages/book.html#toc)* by Harry J. W. Percival is a great resource for learning Django, from creating your first Django application all the way to deploying it to the public internet.
