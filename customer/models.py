from django.db import models

# Create your models here.
from django.db import models
from geoposition.fields import GeopositionField
# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=100)
    position = GeopositionField()
    class Meta:
        verbose_name_plural = 'Customer'
    def __str__(self):
        return self.name

class Bookmark(models.Model):
    title=models.CharField(max_length=100)
    source_name=models.CharField(max_length=100)
    url=models.URLField(max_length=200)
    class Meta:
        verbose_name_plural = 'Bookmark'
    def __str__(self):
        return self.title

class CustomerBookmark(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    bookmark = models.ForeignKey(Bookmark, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = 'CustomerBookmark'
        unique_together= (('customer' , 'bookmark'))
    def __str__(self):
        return self.customer.name + '@' + self.bookmark.title

