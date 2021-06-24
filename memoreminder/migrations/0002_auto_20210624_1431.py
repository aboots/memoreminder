# Generated by Django 3.2.4 on 2021-06-24 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('memoreminder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memouser',
            name='username',
            field=models.CharField(max_length=80, unique=True, verbose_name='یوزرنیم'),
        ),
        migrations.AlterField(
            model_name='post',
            name='creator_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owned_posts', to='memoreminder.memouser', verbose_name='کاربر'),
        ),
    ]
