# Generated by Django 3.0.8 on 2020-07-05 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='content',
            field=models.TextField(blank=True, max_length=2048, null=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
