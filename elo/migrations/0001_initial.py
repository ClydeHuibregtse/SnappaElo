# Generated by Django 2.1.1 on 2018-09-28 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.CharField(max_length=10)),
                ('victors', models.IntegerField(default=0)),
                ('note', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rating', models.IntegerField(default=1000)),
            ],
        ),
        migrations.CreateModel(
            name='RatingChange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=100)),
                ('rating_at_time', models.IntegerField(default=1000)),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='all_ratings',
            field=models.ManyToManyField(to='elo.RatingChange'),
        ),
        migrations.AddField(
            model_name='game',
            name='players',
            field=models.ManyToManyField(related_name='all_players', to='elo.Player'),
        ),
        migrations.AddField(
            model_name='game',
            name='team1',
            field=models.ManyToManyField(related_name='team1', to='elo.Player'),
        ),
        migrations.AddField(
            model_name='game',
            name='team2',
            field=models.ManyToManyField(related_name='team2', to='elo.Player'),
        ),
    ]
