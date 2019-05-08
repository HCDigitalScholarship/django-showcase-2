"""
A model is a definition of a particular entity that we want to store in the database.
A major benefit of using Django is that it abstracts away the details of the SQL queries
necessary to manage your database -- all you have to do is define the model here in
Python, and Django handles the rest.
"""
from django.db import models
from django.urls import reverse


class Text(models.Model):
    # Define a couple of data fields on our text model. A CharField is for character
    # data of a limited length. A TextField is for character data whose length we don't
    # want to limit.
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    body = models.TextField()

    # Keep track of when the model is created. The auto_now_add parameter to the
    # DateTimeField makes sure the field is automatically set at creation.
    created_at = models.DateTimeField(auto_now_add=True)
    # A slug is a journalism term for a unique, human-readable ID for an article. For
    # this model, it will usually be the title and author concatenated together, all in
    # lower case and with spaces replaced by dashes.
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("textviewer:detail", args=[self.slug])
