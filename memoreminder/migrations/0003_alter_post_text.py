# Generated by Django 3.2.4 on 2021-06-24 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memoreminder', '0002_auto_20210624_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(blank=True, max_length=300, null=True, verbose_name='متن'),
        ),
    ]
