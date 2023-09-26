# Generated by Django 4.2.5 on 2023-09-25 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('python_code', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moves', models.JSONField(default=list)),
                ('winner', models.PositiveSmallIntegerField(choices=[(1, 'Player 1'), (2, 'Player 2')], null=True)),
                ('player_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_1_games', to='gameAI.player')),
                ('player_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_2_games', to='gameAI.player')),
                ('tournament_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gameAI.tournament')),
            ],
        ),
    ]
