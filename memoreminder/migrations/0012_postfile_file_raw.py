# Generated by Django 3.2.4 on 2021-07-19 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memoreminder', '0011_auto_20210715_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='postfile',
            name='file_raw',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='لینک فایل'),
        ),
    ]
