# Generated by Django 3.1.7 on 2021-04-20 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0010_auto_20210417_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(default='', upload_to='images'),
            preserve_default=False,
        ),
    ]
