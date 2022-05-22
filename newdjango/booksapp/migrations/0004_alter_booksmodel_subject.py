# Generated by Django 4.0.2 on 2022-05-22 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksapp', '0003_booksmodel_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booksmodel',
            name='subject',
            field=models.IntegerField(choices=[(1, 'C'), (2, 'Java'), (3, 'Python')], default=1),
        ),
    ]
