# Generated by Django 4.2 on 2023-04-19 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_member_cows_in_own'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cows',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cow_name', models.CharField(max_length=255)),
                ('price_for_one', models.IntegerField(null=True)),
            ],
        ),
    ]