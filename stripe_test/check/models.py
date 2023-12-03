from django.db import models


class Item(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self):
        return self.name

