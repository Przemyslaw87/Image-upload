# Generated by Django 3.2.16 on 2023-01-20 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("imageupload", "0004_images_name_file"),
    ]

    operations = [
        migrations.RenameField(
            model_name="images",
            old_name="orginal_name_file",
            new_name="original_name_file",
        ),
    ]
