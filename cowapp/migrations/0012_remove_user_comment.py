# Generated by Django 4.0.3 on 2022-03-29 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cowapp', '0011_alter_amount_info_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='comment',
        ),
    ]
