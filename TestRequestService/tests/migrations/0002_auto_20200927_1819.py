# Generated by Django 3.1.1 on 2020-09-27 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='tests',
            field=models.JSONField(default={}),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Test',
        ),
    ]