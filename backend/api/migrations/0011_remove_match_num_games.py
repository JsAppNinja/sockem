# Generated by Django 2.2.3 on 2019-07-30 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20190730_2043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='num_games',
        ),
    ]