from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    quantity = models.IntegerField()
    is_published = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table='book'
