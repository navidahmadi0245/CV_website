# Generated by Django 4.2.11 on 2024-05-19 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_counted_view_alter_post_created_datetime_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='created_datetime',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='published_datetime',
            new_name='published_date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='updated_datetime',
            new_name='updated_date',
        ),
    ]
