# Generated by Django 3.2.5 on 2021-08-19 22:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_curso_curso_publicado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='curso_publicado',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 19, 17, 18, 54, 759736), verbose_name='fecha de publicacion'),
        ),
    ]
