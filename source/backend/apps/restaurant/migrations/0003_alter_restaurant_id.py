# Generated by Django 3.2.7 on 2021-09-20 20:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_auto_20210920_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
