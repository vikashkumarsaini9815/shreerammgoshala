# Generated by Django 3.2.10 on 2022-03-02 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cowapp', '0003_alter_amount_info_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
