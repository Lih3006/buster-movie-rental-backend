# Generated by Django 4.2.4 on 2023-08-09 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=127)),
                ('duration', models.CharField(default=None, max_length=10, null=True)),
                ('rating', models.CharField(choices=[('G', 'G'), ('PG', 'Pg'), ('PG-13', 'Pg 13'), ('R', 'R'), ('NC_17', 'Nc 17')], default='G', max_length=20)),
                ('synopsis', models.TextField(default=None, null=True)),
            ],
        ),
    ]
