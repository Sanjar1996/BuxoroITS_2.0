# Generated by Django 3.2.6 on 2021-08-14 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0013_alter_aboutmaydon_maydon'),
    ]

    operations = [
        migrations.CreateModel(
            name='XodimModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('lavozim', models.CharField(max_length=50)),
                ('birth_day', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='image/')),
            ],
        ),
    ]
