# Generated by Django 2.2.3 on 2019-09-18 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0017_day_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='day_played',
            field=models.IntegerField(null=True),
        ),
    ]
