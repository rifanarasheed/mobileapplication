from django.db import models

# Create your models here.
class Brands(models.Model):
    brand_name = models.CharField(max_length=120,unique=True)
    def __str__(self):
        return self.brand_name

class Mobile(models.Model):
    model_name = models.CharField(max_length=120)
    brand = models.ForeignKey(Brands,on_delete = models.CASCADE)      # making brand as foreign so to get data from other model known as Brands and on_delete() -> if any changes made in brands model, it will reflect mobile model also
    price = models.IntegerField(null=False)
    specs = models.CharField(max_length=120)
    description = models.CharField(max_length=120)
    img = models.ImageField(upload_to='images')   # images will be uploaded into folder known as images, we dont need to create separetly

    def __str__(self):
        return self.model_name

class Order(models.Model):
    # in the form, only address need to be entered because product and user should come by default.
    product = models.ForeignKey(Mobile,on_delete=models.CASCADE)
    address = models.CharField(max_length=200) 
    user = models.CharField(max_length=120)
    choices = [
        ("ORDERED","ordered"),
        ("DISPATCHED","dispatched"),
        ("DELIVERED","delivered"),
        ("CANCELLED","Cancelled")
    ]
    status = models.CharField(max_length=40,choices=choices,default="ordered")

