# Generated by Django 4.0 on 2021-12-19 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0012_rename_attend_joined_attendance_user_joined'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='date_now',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
