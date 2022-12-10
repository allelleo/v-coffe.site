# Generated by Django 3.0 on 2022-12-09 19:06

from django.db import migrations, models
import home.Logic


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20221209_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='preview_photo',
            field=models.ImageField(upload_to=home.Logic.path_and_rename),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='url',
            field=models.CharField(max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]