# Generated by Django 2.1.7 on 2019-03-23 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_claim_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='claim',
            old_name='PREDICTION',
            new_name='INDICATOR',
        ),
    ]