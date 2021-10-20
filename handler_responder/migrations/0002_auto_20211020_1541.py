# Generated by Django 3.2.8 on 2021-10-20 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [('handler_responder', '0001_initial')]

    operations = [
        migrations.RenameField(
            model_name='trigger', old_name='word', new_name='phrase'
        ),
        migrations.AlterField(
            model_name='response',
            name='trigger',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='responses',
                to='handler_responder.trigger',
            ),
        ),
    ]