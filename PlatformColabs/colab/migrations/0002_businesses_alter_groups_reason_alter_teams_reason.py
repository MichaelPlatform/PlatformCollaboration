# Generated by Django 4.2.5 on 2023-09-24 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colab', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Businesses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=50)),
                ('params_1', models.CharField(max_length=50)),
                ('params_2', models.CharField(max_length=50)),
                ('params_3', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='groups',
            name='reason',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='teams',
            name='reason',
            field=models.CharField(max_length=50),
        ),
    ]