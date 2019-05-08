"""
Production settings. The main settings module conditionally imports these when it
detects that it is running on the staging or production servers.
"""
import os


DEBUG = False
SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]
ALLOWED_HOSTS = [os.environ["DJANGO_SITENAME"]]
