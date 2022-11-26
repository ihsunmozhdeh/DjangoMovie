# Generated by Django 4.1.3 on 2022-11-25 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0008_review_status_alter_review_movie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='movie',
        ),
        migrations.RemoveField(
            model_name='actor',
            name='role',
        ),
        migrations.AddField(
            model_name='actor',
            name='movies',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='actors', to='movie.movie'),
        ),
        migrations.AddField(
            model_name='movie',
            name='actor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='actor', to='movie.actor'),
        ),
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='director', to='movie.actor'),
        ),
    ]
