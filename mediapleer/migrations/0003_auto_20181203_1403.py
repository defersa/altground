# Generated by Django 2.1.3 on 2018-12-03 11:03

from django.db import migrations


class Migration(migrations.Migration):

    atomic = False

    dependencies = [
        ('mediapleer', '0002_auto_20181203_1351'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Albums',
            new_name='Album',
        ),
        migrations.RenameModel(
            old_name='Bands',
            new_name='Band',
        ),
        migrations.RenameModel(
            old_name='Concerts',
            new_name='Concert',
        ),
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
        migrations.RenameModel(
            old_name='Videos',
            new_name='Video',
        ),
    ]