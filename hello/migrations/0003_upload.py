# Generated by Django 4.1.7 on 2023-02-17 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_alter_post_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
            ],
        ),
    ]
