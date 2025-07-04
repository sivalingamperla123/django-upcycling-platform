from django.db import models
import os
# Create your models here.

class UsersModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=100)
    contact = models.IntegerField()
    address = models.CharField(max_length=100)
    profile = models.FileField(upload_to=os.path.join('static', 'userprofiles'))
    proof = models.FileField(upload_to=os.path.join('static', 'proof'),null=True)
    status = models.CharField(max_length=100,default='pending',null=True)
    

    def __str__(self):  
        return self.name
    
    class Meta:
        db_table = "UsersModel"


class UploadProductModel(models.Model):
    product_name = models.CharField(max_length=100)
    product_desc = models.TextField()
    product_img = models.FileField(upload_to=os.path.join('static', 'ProductImages'))
    upload_time = models.DateTimeField()
    uploaderemail = models.EmailField()
    category = models.CharField(max_length=100)
    status = models.CharField(max_length=100,default='Available')
    def __str__(self):
        return self.product_name
    class Meta:
        db_table = "UploadProductModel"


class ChatModel(models.Model):
    cid =models.IntegerField(null=True)
    remail = models.EmailField(null=True)
    email = models.EmailField(null=True)
    chat =  models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.email
    class  Meta:
        db_table= "ChatModel"


class CollectedProducts(models.Model):
    product_name = models.CharField(max_length=100)
    product_desc = models.TextField()
    product_img = models.FileField(upload_to=os.path.join('static', 'ProductImages'))
    upload_time = models.DateTimeField()
    uploaderemail = models.EmailField()
    category = models.CharField(max_length=100)
    # status = models.CharField(max_length=100,default='Pending')
    collectedemail=models.EmailField()

    def __str__(self):
        return self.product_name
    class Meta:
        db_table = "CollectedProducts"