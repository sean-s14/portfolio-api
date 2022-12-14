# Generated by Django 4.1 on 2022-09-07 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imageURI', models.TextField(blank=True, null=True)),
                ('title', models.CharField(max_length=150, unique=True)),
                ('link', models.URLField(max_length=150, unique=True)),
            ],
        ),
    ]
