# Generated by Django 5.0.6 on 2024-06-26 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
