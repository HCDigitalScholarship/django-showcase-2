# Generated by Django 2.2 on 2019-04-10 14:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [("textviewer", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="text",
            name="author",
            field=models.CharField(default="", max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="text",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="text",
            name="slug",
            field=models.SlugField(default="change-me", unique=True),
            preserve_default=False,
        ),
    ]
