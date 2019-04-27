# Generated by Django 2.1.7 on 2019-04-08 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0011_note_saving'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('claimId', models.CharField(max_length=50)),
                ('claimNumber', models.CharField(max_length=50)),
                ('claimNoteID', models.CharField(max_length=50)),
                ('reviewer', models.CharField(max_length=50)),
                ('indicators', models.TextField(max_length=200)),
                ('validation', models.TextField(max_length=200)),
                ('probability', models.CharField(max_length=10)),
                ('customer', models.CharField(max_length=50)),
                ('saving', models.CharField(max_length=50)),
                ('comments', models.TextField(max_length=1000)),
            ],
        ),
    ]