# Generated by Django 3.2.8 on 2021-10-10 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                (
                    'id',
                    models.CharField(
                        max_length=16, primary_key=True, serialize=False
                    ),
                ),
                ('name', models.CharField(max_length=255)),
                (
                    'channel_type',
                    models.CharField(
                        choices=[
                            ('private', 'Public'),
                            ('public', 'Private'),
                            ('direct', 'Direct'),
                        ],
                        max_length=7,
                    ),
                ),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        )
    ]
