# Generated by Django 2.1.7 on 2019-05-16 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20190516_1311'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vote',
            old_name='position',
            new_name='post',
        ),
    ]
