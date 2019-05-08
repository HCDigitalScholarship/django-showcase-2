"""
Configuration of the admin site for the textviewer app.

Whenever you add a new model, you should register it here.
"""
from django.contrib import admin

from . import models


class TextAdmin(admin.ModelAdmin):
    # This setting ensures that when you enter a text's title and author, the slug is
    # automatically generated as you type.
    prepopulated_fields = {"slug": ("title", "author")}


# Register the model with the given ModelAdmin class. Usually you don't need a custom
# ModelAdmin class, and you can just write admin.site.register(models.MyModel).
admin.site.register(models.Text, TextAdmin)
