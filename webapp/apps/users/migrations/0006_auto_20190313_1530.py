# Generated by Django 2.1.7 on 2019-03-13 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("users", "0005_auto_20190313_1528")]

    operations = [
        migrations.RenameField(model_name="project", old_name="name", new_name="title")
    ]
