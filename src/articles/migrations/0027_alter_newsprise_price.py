# Generated by Django 3.2.6 on 2021-08-19 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0026_auto_20210819_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsprise',
            name='price',
            field=models.FloatField(),
        ),
    ]
