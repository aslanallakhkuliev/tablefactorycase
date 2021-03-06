# Generated by Django 3.1.7 on 2021-03-04 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0005_auto_20210304_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foot',
            name='length',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='foot',
            name='radius',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='foot',
            name='width',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
