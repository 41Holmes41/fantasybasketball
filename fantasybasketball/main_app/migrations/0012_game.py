# Generated by Django 2.2.3 on 2019-09-17 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_auto_20190917_1740'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points_scored', models.IntegerField(null=True)),
                ('rebounds', models.IntegerField(null=True)),
                ('assists', models.IntegerField(null=True)),
                ('steals', models.IntegerField(null=True)),
                ('blocks', models.IntegerField(null=True)),
                ('turnovers', models.IntegerField(null=True)),
                ('threepointers', models.IntegerField(null=True)),
                ('player', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.Player')),
                ('team', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.Team')),
            ],
        ),
    ]
