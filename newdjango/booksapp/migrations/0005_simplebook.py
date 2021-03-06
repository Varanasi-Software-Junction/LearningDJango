# Generated by Django 4.0.2 on 2022-05-22 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksapp', '0004_alter_booksmodel_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='SimpleBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookname', models.CharField(max_length=200)),
                ('subject', models.IntegerField(choices=[(1, 'C'), (2, 'Java'), (3, 'Python')], default=1)),
                ('price', models.IntegerField()),
                ('cover', models.ImageField(upload_to='static/')),
            ],
        ),
    ]
