# Generated by Django 4.2 on 2023-05-01 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortenerapp', '0005_url_delete_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='uuid',
            field=models.CharField(max_length=5, unique=True),
        ),
    ]