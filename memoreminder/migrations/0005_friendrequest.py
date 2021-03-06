# Generated by Django 3.2.4 on 2021-07-01 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('memoreminder', '0004_memouser_token'),
    ]

    operations = [
        migrations.CreateModel(
            name='FriendRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='زمان ساخت')),
                ('modified', models.DateTimeField(auto_now=True, db_index=True, verbose_name='آخرین زمان تغییر')),
                ('status', models.CharField(choices=[('accepted', 'تایید'), ('rejected', 'رد'), ('pending', 'در حال بررسی')], max_length=50, verbose_name='وضعیت')),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend_request_sent', to='memoreminder.memouser', verbose_name='از کاربر')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend_request_received', to='memoreminder.memouser', verbose_name='به کاربر')),
            ],
            options={
                'verbose_name': 'درخواست دوستی',
                'verbose_name_plural': 'درخواست های دوستی',
            },
        ),
    ]
