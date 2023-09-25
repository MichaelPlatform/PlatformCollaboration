# Generated by Django 4.2.5 on 2023-09-25 16:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colab', '0007_teams_fundraiser_alter_businesses_key_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_key', models.IntegerField(default=15800333, validators=[django.core.validators.MaxValueValidator(8)])),
                ('username', models.TextField(default=None)),
                ('message', models.TextField(default=None)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='businesses',
            name='key',
            field=models.IntegerField(default=15800333, validators=[django.core.validators.MaxValueValidator(8)]),
        ),
        migrations.AlterField(
            model_name='businessesmanager',
            name='key',
            field=models.IntegerField(default=15800333, validators=[django.core.validators.MaxValueValidator(8)]),
        ),
        migrations.AlterField(
            model_name='groups',
            name='key',
            field=models.IntegerField(default=15800333, validators=[django.core.validators.MaxValueValidator(8)]),
        ),
        migrations.AlterField(
            model_name='groupsmanager',
            name='key',
            field=models.IntegerField(default=15800333, validators=[django.core.validators.MaxValueValidator(8)]),
        ),
        migrations.AlterField(
            model_name='teams',
            name='key',
            field=models.IntegerField(default=15800333, validators=[django.core.validators.MaxValueValidator(8)]),
        ),
        migrations.AlterField(
            model_name='teamsmanager',
            name='key',
            field=models.IntegerField(default=15800333, validators=[django.core.validators.MaxValueValidator(8)]),
        ),
    ]
