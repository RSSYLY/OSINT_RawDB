# Generated by Django 4.2 on 2024-01-31 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_db', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rawarticlesdata',
            name='word_cloud_img',
            field=models.ImageField(blank=True, null=True, upload_to='word_cloud/'),
        ),
    ]
