# Generated by Django 2.2.4 on 2019-08-16 23:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 16, 23, 3, 11, 413929, tzinfo=utc), verbose_name='Fecha de publicación'),
        ),
    ]
