# Generated by Django 5.0.1 on 2024-01-06 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
