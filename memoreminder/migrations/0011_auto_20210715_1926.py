# Generated by Django 3.2.4 on 2021-07-15 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('memoreminder', '0010_auto_20210715_1647'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='commentlike',
            unique_together={('comment', 'memo_user')},
        ),
        migrations.AlterUniqueTogether(
            name='postlike',
            unique_together={('post', 'memo_user')},
        ),
    ]
