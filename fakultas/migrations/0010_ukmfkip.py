# Generated by Django 4.1.1 on 2022-10-11 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fakultas', '0009_ruanganfkip'),
    ]

    operations = [
        migrations.CreateModel(
            name='UKMFkip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
            ],
        ),
    ]
