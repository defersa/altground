# Generated by Django 2.1.3 on 2018-12-11 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mediapleer', '0005_auto_20181203_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='videos',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mediapleer.Video'),
        ),
    ]