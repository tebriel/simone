# Generated by Django 3.2.8 on 2021-10-21 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [('slacker', '0002_auto_20211010_2218')]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='channel_type',
            field=models.CharField(
                choices=[
                    ('public', 'Public'),
                    ('private', 'Private'),
                    ('direct', 'Direct'),
                ],
                max_length=7,
            ),
        ),
        migrations.AlterUniqueTogether(name='channel', unique_together=set()),
        migrations.RemoveField(model_name='channel', name='team_id'),
    ]