# Generated by Django 4.1.1 on 2022-10-11 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fakultas', '0012_matakuliahfkip'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProdiFkip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
            ],
        ),
    ]
