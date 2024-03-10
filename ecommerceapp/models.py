from django.db import models

# Create your models here.
class Contact(models.Model):
    frist_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=20)
    email=models.EmailField()
    mob=models.IntegerField()
    address=models.TextField(max_length=300)
    query=models.TextField(max_length=500)

    def __str__(self) :
        return self.frist_name

class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    subcategory=models.CharField(max_length=100)
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=300)
    image=models.ImageField(upload_to='images/images', default="")

    def __str__(self):
        return self.product_name
    
class Subcriber(models.Model):
    subcriber_detailes=models.EmailField()


    
    def __str__(self) :
        return self.subcriber_detailes
    

class blog(models.Model):
    title=models.CharField(max_length=70)
    discription=models.TextField()
    author_name=models.CharField(max_length=80)
    image=models.ImageField(upload_to='blog',blank=True,null=True)
    timestamp=models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.title