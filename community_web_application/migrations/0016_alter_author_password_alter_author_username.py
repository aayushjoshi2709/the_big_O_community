# Generated by Django 4.2.6 on 2023-11-16 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community_web_application', '0015_alter_author_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='password',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='author',
            name='username',
            field=models.CharField(max_length=50),
        ),
    ]
