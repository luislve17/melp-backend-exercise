# Generated by Django 3.2.7 on 2021-09-22 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_alter_restaurant_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='rating',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
