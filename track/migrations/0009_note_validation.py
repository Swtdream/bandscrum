# Generated by Django 2.1.7 on 2019-04-05 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0008_auto_20190404_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='validation',
            field=models.TextField(default=' ', max_length=200),
            preserve_default=False,
        ),
    ]