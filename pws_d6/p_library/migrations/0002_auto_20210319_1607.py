# Generated by Django 3.1.7 on 2021-03-19 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='count',
            new_name='copy_count',
        ),
    ]
