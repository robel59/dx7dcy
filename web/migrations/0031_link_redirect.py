# Generated by Django 4.2.4 on 2024-07-01 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0030_useraccess_session_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='redirect',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
