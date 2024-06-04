from django.conf import settings
from django.db import models
from django.shortcuts import reverse
from django.utils import timezone
import pathlib
from os import path
from uuid import uuid4


def assign(instance, file_name):
    unique_key = uuid4()
    return str(unique_key) + "/" + file_name


class Item(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    # img_url=models.FileField(max_length=255,null=False, upload_to=assign)
    

    def __str__(self):
        return f'{self.id}, {self.name}, {self.description}'

class ImagesItem(models.Model):
    id = models.IntegerField(primary_key=True)
    item_id = models.ManyToManyField(Item)
    alt_text = models.CharField(max_length=255)
    img_url=models.FileField(max_length=255,null=False, upload_to=assign)
    order_no=models.IntegerField()

    def __str__(self):
        return f'{self.id}, {self.img_url}'

class Packaging(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.IntegerField()

    def __str__(self):
        return str(self.type)


class Color(models.Model):
    id = models.IntegerField(primary_key=True)
    color_code = models.IntegerField()
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Users(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    email = models.EmailField(
        max_length=100, unique=True, default="something@gmail.com"
    )
    


class ItemPack(models.Model):
    id = models.IntegerField(primary_key=True)
    item_id = models.ManyToManyField(Item)
    packaging_id = models.ManyToManyField(Packaging)
    price = models.IntegerField()


class ItemPackColor(models.Model):
    id = models.IntegerField(primary_key=True)
    item_pack_id = models.ForeignKey(ItemPack, on_delete=models.CASCADE)
    color_id = models.ForeignKey(Color, on_delete=models.CASCADE)


class Order(models.Model):
    id = models.IntegerField(primary_key=True)
    order_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    # will update every time
    updated_at = models.DateTimeField(auto_now=True)


class OrderItem(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    description = models.TextField()
    color_code = models.IntegerField()
    qty = models.IntegerField()
    ordered_at = models.DateTimeField(default=timezone.now)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
