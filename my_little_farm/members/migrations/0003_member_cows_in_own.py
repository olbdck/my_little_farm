# Generated by Django 4.2 on 2023-04-17 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_member_joined_date_member_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='cows_in_own',
            field=models.IntegerField(null=True),
        ),
    ]
