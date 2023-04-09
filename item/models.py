from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length= 50,null=False,blank=False)
    
    class  Meta:
        ordering = ['name',]
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Item(models.Model):
    category = models.ForeignKey(Category,related_name='items',on_delete=models.CASCADE)
    name = models.CharField(max_length=60,null=False,blank=False)
    description = models.TextField(null=False,blank=True)
    image = models.ImageField(upload_to='item_images',blank=False,null=False)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User,related_name='items',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name',]

    def __str__(self):
        return self.name
