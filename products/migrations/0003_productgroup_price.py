# Generated by Django 3.1.5 on 2021-01-28 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210127_2334'),
    ]

    operations = [
        migrations.AddField(
            model_name='productgroup',
            name='price',
            field=models.PositiveIntegerField(null=True),
        ),
    ]