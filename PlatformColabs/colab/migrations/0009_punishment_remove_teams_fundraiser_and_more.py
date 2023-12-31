# Generated by Django 4.2.5 on 2023-09-25 18:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colab', '0008_messages_alter_businesses_key_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Punishment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('punishment_type', models.TextField(default=None)),
                ('account_key', models.TextField(default=None)),
                ('reason', models.TextField(default='Not reason given.')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='teams',
            name='fundraiser',
        ),
        migrations.AddField(
            model_name='businessesmanager',
            name='ban_list',
            field=models.TextField(default=[]),
        ),
        migrations.AddField(
            model_name='businessesmanager',
            name='current_project',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='businessesmanager',
            name='meetings',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='groupsmanager',
            name='ban_list',
            field=models.TextField(default=[]),
        ),
        migrations.AddField(
            model_name='messages',
            name='group_key',
            field=models.IntegerField(default=None, validators=[django.core.validators.MaxValueValidator(8)]),
        ),
        migrations.AddField(
            model_name='messages',
            name='sender',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='teamsmanager',
            name='ban_list',
            field=models.TextField(default=[]),
        ),
        migrations.AddField(
            model_name='teamsmanager',
            name='fundraiser',
            field=models.TextField(default=[]),
        ),
        migrations.AlterField(
            model_name='businesses',
            name='key',
            field=models.IntegerField(default=53229620, validators=[django.core.validators.MaxValueValidator(8)]),
        ),
        migrations.AlterField(
            model_name='businessesmanager',
            name='key',
            field=models.IntegerField(default=53229620, validators=[django.core.validators.MaxValueValidator(8)]),
        ),
        migrations.AlterField(
            model_name='businessesmanager',
            name='max_members',
            field=models.IntegerField(default=300),
        ),
        migrations.AlterField(
            model_name='businessesmanager',
            name='members',
            field=models.TextField(default=[]),
        ),
        migrations.AlterField(
            model_name='groups',
            name='key',
            field=models.IntegerField(default=53229620, validators=[django.core.validators.MaxValueValidator(8)]),
        ),
        migrations.AlterField(
            model_name='groupsmanager',
            name='key',
            field=models.IntegerField(default=53229620, validators=[django.core.validators.MaxValueValidator(8)]),
        ),
        migrations.AlterField(
            model_name='groupsmanager',
            name='members',
            field=models.TextField(default=[]),
        ),
        migrations.AlterField(
            model_name='messages',
            name='account_key',
            field=models.IntegerField(default=None, validators=[django.core.validators.MaxValueValidator(8)]),
        ),
        migrations.AlterField(
            model_name='teams',
            name='key',
            field=models.IntegerField(default=53229620, validators=[django.core.validators.MaxValueValidator(8)]),
        ),
        migrations.AlterField(
            model_name='teamsmanager',
            name='key',
            field=models.IntegerField(default=53229620, validators=[django.core.validators.MaxValueValidator(8)]),
        ),
        migrations.AlterField(
            model_name='teamsmanager',
            name='max_members',
            field=models.IntegerField(default=50),
        ),
        migrations.AlterField(
            model_name='teamsmanager',
            name='members',
            field=models.TextField(default=[]),
        ),
    ]
