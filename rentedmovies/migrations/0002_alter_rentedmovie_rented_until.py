# Generated by Django 4.2.6 on 2023-10-13 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentedmovies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentedmovie',
            name='rented_until',
            field=models.DateTimeField(),
        ),
    ]