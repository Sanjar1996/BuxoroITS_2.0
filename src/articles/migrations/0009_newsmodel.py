# Generated by Django 3.2.6 on 2021-08-12 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image/')),
                ('title', models.CharField(max_length=250)),
                ('summary', models.CharField(max_length=250)),
                ('body', models.TextField()),
            ],
        ),
    ]