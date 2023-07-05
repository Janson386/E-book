from django.db import models

# Create your models here.


class custemerdetaildb(models.Model):
    username = models.CharField(max_length=30, null=True, blank=True)
    email = models.CharField(max_length=30, null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    conformpassword = models.CharField(max_length=100, null=True, blank=True)


class carttdb(models.Model):
    user = models.CharField(max_length=30, null=True, blank=True)
    productname = models.CharField(max_length=30, null=True, blank=True)
    productprice = models.CharField(max_length=100, null=True, blank=True)
    productlanguage = models.CharField(max_length=100, null=True, blank=True)
    pdf=models.FileField(upload_to="document",null=True,blank=True)
    productimagee=models.ImageField(upload_to="profile",null=True,blank=True)


class paymentdetaildb(models.Model):
    fullname = models.CharField(max_length=30, null=True, blank=True)
    emaill = models.CharField(max_length=30, null=True, blank=True)
    phonenumber = models.IntegerField(null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
