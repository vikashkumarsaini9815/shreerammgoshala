# Generated by Django 3.2.10 on 2022-03-02 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cowapp', '0004_alter_user_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='contact',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
