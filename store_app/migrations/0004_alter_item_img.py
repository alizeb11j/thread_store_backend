# Generated by Django 4.2.13 on 2024-06-02 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0003_item_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='img',
            field=models.FileField(upload_to=''),
        ),
    ]
