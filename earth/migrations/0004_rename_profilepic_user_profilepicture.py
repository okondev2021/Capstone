# Generated by Django 3.2.9 on 2022-05-27 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('earth', '0003_user_profilepic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='ProfilePic',
            new_name='ProfilePicture',
        ),
    ]
