# Generated by Django 5.0.6 on 2024-07-29 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='Album_Name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='album',
            name='Rating',
            field=models.CharField(choices=[('One', '1'), ('Two', '2'), ('Three', '3'), ('Four', '4'), ('Five', '5')], default='1', max_length=5),
        ),
    ]