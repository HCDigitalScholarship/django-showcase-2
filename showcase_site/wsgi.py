"""
WSGI config for showcase project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "showcase_site.settings")

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
