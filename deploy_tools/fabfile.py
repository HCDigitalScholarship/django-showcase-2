"""
The automated deployment script, which runs all the commands necessary to deploy the
code to our staging and production servers.

Don't try to run this file directly; use the top-level ./deploy script instead.

Heavily based on the example from the "Automated Deployment with Fabric" chapter of
"Obey the Testing Goat" by Harry J. W. Percival.
(https://www.obeythetestinggoat.com/book/chapter_automate_deployment_with_fabric.html)
"""
import random

from fabric.contrib.files import append, exists
from fabric.api import cd, env, local, run


REPO_URL = "https://github.com/HCDigitalScholarship/django-showcase-2.git"


def deploy():
    site_folder = "/srv/sites/{0.host}".format(env)
    run("mkdir -p " + site_folder)
    with cd(site_folder):
        _get_latest_source()
        _update_virtualenv()
        _create_or_update_dotenv()
        _update_static_files()
        _update_database()
        _restart_service()


def _get_latest_source():
    if exists(".git"):
        run("git fetch")
    else:
        run("git clone {} .".format(REPO_URL))

    current_commit = local("git log -n 1 --format=%H", capture=True)
    run("git reset --hard " + current_commit)
    run("sudo chown -R www-data: .")


def _update_virtualenv():
    if not exists(".venv/bin/pip"):
        run("virtualenv .venv --python=python3")
    run("./.venv/bin/pip install -r requirements.txt")


def _create_or_update_dotenv():
    append(".env", "DJANGO_DEBUG_FALSE=y")
    append(".env", "DJANGO_SITENAME=" + env.host)
    current_contents = run("cat .env")
    if "DJANGO_SECRET_KEY" not in current_contents:
        new_secret = "".join(
            random.SystemRandom().choices("abcdefghijklmnopqrstuvwxyz0123456789", k=50)
        )
        append(".env", "DJANGO_SECRET_KEY=" + new_secret)


def _update_static_files():
    run("./.venv/bin/python3 manage.py collectstatic --noinput")


def _update_database():
    run("./.venv/bin/python3 manage.py migrate --noinput")


def _restart_service():
    run("sudo service uwsgi restart")
