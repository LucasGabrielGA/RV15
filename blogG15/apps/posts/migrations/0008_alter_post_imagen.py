# Generated by Django 5.1.1 on 2024-10-20 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_alter_post_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.ImageField(blank=True, default='../static/post_default.jpg', null=True, upload_to='media'),
        ),
    ]