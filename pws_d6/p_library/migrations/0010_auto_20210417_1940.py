# Generated by Django 3.1.7 on 2021-04-17 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0009_remove_reader_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='reader',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='get_book', to='p_library.reader'),
        ),
    ]