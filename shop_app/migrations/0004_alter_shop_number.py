# Generated by Django 3.2.4 on 2021-06-17 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0003_alter_shop_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='number',
            field=models.BigIntegerField(default=0),
        ),
    ]
