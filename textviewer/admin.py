from django.contrib import admin

from . import models


class TextAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title", "author")}


admin.site.register(models.Text, TextAdmin)
