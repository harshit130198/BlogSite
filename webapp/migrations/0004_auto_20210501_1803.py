# Generated by Django 3.1.4 on 2021-05-01 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20210501_1608'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='pub_date',
            new_name='Pub_date',
        ),
    ]
