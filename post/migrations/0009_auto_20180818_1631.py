# Generated by Django 2.1 on 2018-08-18 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_auto_20180816_2356'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gdsmodel',
            options={'ordering': ['-date']},
        ),
    ]