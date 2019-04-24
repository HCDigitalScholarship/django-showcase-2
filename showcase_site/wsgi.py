"""
WSGI config for showcase project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "showcase_site.settings")

# When deployed to staging and production, the Django application relies on a set of
# environment variables defined in a file called .env in the root directory of the
# project. This file is created by the deployment script in deploy_tools/fabfile.py. If
# the file exists, we want to add each line in it as an environment variable so the
# Django application is configured correctly.
#
# This is a slightly janky way to do it--normally we would want to define .env as an
# environment file in a systemd unit config, but since we're piggybacking on the built-
# in uWSGI service and not writing our own, we don't have that option.
# [iafisher, 2019-04-24]
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if os.path.exists(os.path.join(BASE_DIR, ".env")):
    with open(os.path.join(BASE_DIR, ".env"), "r", encoding="utf-8") as f:
        for line in f:
            try:
                key, val = line.strip().split("=", maxsplit=1)
            except ValueError:
                pass
            else:
                os.environ[key] = val

application = get_wsgi_application()
