# Generated by Django 2.2.4 on 2019-09-26 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elementos', '0006_auto_20190926_0618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pelicula',
            name='actor',
        ),
        migrations.AddField(
            model_name='pelicula',
            name='actor',
            field=models.ManyToManyField(to='elementos.Actor'),
        ),
    ]
