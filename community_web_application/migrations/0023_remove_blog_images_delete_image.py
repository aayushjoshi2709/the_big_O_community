# Generated by Django 4.2.6 on 2023-11-17 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community_web_application', '0022_alter_blog_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='images',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
