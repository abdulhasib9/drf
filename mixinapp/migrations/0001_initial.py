# Generated by Django 5.0.3 on 2024-03-26 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=234)),
                ('lastName', models.CharField(max_length=230)),
            ],
        ),
    ]
