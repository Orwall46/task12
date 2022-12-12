import os
from PIL import Image
from django.db import models
from .services import make_thumbnail


def get_item_path(instance, filename):
    images = 'item_images'

    return os.path.join(images, "%s" % fr"{instance.article}", filename)


class Item(models.Model):
    CHOICES = (
        ('В наличии', 'В наличии'),
        ('Под заказ', 'Под заказ'),
        ('Ожидается поступление', 'Ожидается поступление'),
        ('Нет в наличии', 'Нет в наличии'),
        ('Не производится', 'Не производится'),
    )

    name = models.CharField(max_length=150, verbose_name='Название товара')
    article = models.IntegerField(verbose_name='Артикул')
    price = models.PositiveIntegerField(blank=True, null=True)
    status = models.CharField(choices=CHOICES, max_length=21)
    image = models.ImageField(upload_to=get_item_path, verbose_name='Изображение')
    first_format = models.CharField(
        verbose_name='Старый формат',
        max_length=5,
        blank=True,
        null=True
    )

    def save(self, *args, **kwargs):
        with Image.open(self.image) as im:
            self.first_format = str(im.format)
        super().save(*args, **kwargs)
        self.image = make_thumbnail(self.image)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.name}"

    def get_format(self):
        formats = []
        formats.append(str(self.first_format).lower())
        with Image.open(self.image) as im:
            formats.append(str(im.format).lower())
        return formats
