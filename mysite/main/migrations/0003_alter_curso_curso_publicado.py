# Generated by Django 3.2.5 on 2021-08-12 22:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_curso_curso_publicado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='curso_publicado',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 12, 17, 9, 10, 803954), verbose_name='fecha de publicacion'),
        ),
    ]