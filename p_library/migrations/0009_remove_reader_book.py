# Generated by Django 3.1.7 on 2021-04-11 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0008_auto_20210411_1949'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reader',
            name='book',
        ),
    ]