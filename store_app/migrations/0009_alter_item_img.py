# Generated by Django 4.2.13 on 2024-06-04 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0008_item_img_alter_item_img_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='img',
            field=models.FileField(max_length=255, upload_to=''),
        ),
    ]