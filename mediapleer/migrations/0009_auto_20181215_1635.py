# Generated by Django 2.1.3 on 2018-12-15 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mediapleer', '0008_auto_20181215_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='per',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
