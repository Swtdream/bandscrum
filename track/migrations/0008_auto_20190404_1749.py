# Generated by Django 2.1.7 on 2019-04-05 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0007_auto_20190404_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='claimId',
            field=models.CharField(default=' ', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='note',
            name='claimNumber',
            field=models.CharField(default=' ', max_length=50),
            preserve_default=False,
        ),
    ]
