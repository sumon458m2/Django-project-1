# Generated by Django 3.1.1 on 2020-12-02 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('child_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='children',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]
