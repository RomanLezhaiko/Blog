# Generated by Django 4.1.5 on 2023-02-12 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_remove_post_status_delete_post_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published'), (2, 'Deleted')], default=1),
        ),
    ]
