# Generated by Django 3.2.16 on 2023-01-18 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imageupload', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Image',
            new_name='Images',
        ),
    ]