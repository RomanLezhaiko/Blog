# Generated by Django 4.1.5 on 2023-02-11 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_rename_satus_delete_post_status_delete'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='status_delete',
        ),
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.IntegerField(choices=[(0, 'Published'), (1, 'Deleted')], default=0),
        ),
    ]
