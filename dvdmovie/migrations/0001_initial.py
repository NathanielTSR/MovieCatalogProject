# Generated by Django 2.1.3 on 2018-11-25 13:30

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DVD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('dateadded', models.DateField(default=datetime.date.today)),
                ('version', models.CharField(max_length=64)),
                ('diskcondition', models.CharField(max_length=256)),
                ('note', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('name', models.CharField(max_length=64, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('name', models.CharField(max_length=64, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('releasedate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='PartOfSeries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=50)),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dvdmovie.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('givenname', models.CharField(max_length=128)),
                ('surname', models.CharField(max_length=128)),
                ('prefix', models.CharField(max_length=64)),
                ('suffix', models.CharField(max_length=64)),
                ('nameknownby', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('movies', models.ManyToManyField(through='dvdmovie.PartOfSeries', to='dvdmovie.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Star',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=128)),
                ('actor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acting_in', to='dvdmovie.Person')),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dvdmovie.Movie')),
            ],
        ),
        migrations.AddField(
            model_name='partofseries',
            name='series_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dvdmovie.Series'),
        ),
        migrations.AddField(
            model_name='movie',
            name='directors',
            field=models.ManyToManyField(related_name='director', to='dvdmovie.Person'),
        ),
        migrations.AddField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(to='dvdmovie.Genre'),
        ),
        migrations.AddField(
            model_name='movie',
            name='stars',
            field=models.ManyToManyField(related_name='star', through='dvdmovie.Star', to='dvdmovie.Person'),
        ),
        migrations.AddField(
            model_name='dvd',
            name='audio',
            field=models.ManyToManyField(related_name='audio', to='dvdmovie.Language'),
        ),
        migrations.AddField(
            model_name='dvd',
            name='movies',
            field=models.ManyToManyField(to='dvdmovie.Movie'),
        ),
        migrations.AddField(
            model_name='dvd',
            name='subtitle',
            field=models.ManyToManyField(related_name='subs', to='dvdmovie.Language'),
        ),
        migrations.AlterUniqueTogether(
            name='star',
            unique_together={('actor_id', 'movie_id', 'role')},
        ),
        migrations.AlterUniqueTogether(
            name='partofseries',
            unique_together={('series_id', 'movie_id')},
        ),
    ]