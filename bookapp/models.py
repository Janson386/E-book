from django.db import models

# Create your models here.
class acdb(models.Model):
    categoryname=models.CharField(max_length=30,null=True,blank=True)
    # genres=models.CharField(max_length=30,null=True,blank=True)
    description=models.CharField(max_length=100,null=True,blank=True)
    imagee=models.ImageField(upload_to="profile",null=True,blank=True)


class gndb(models.Model):
    GenreName=models.CharField(max_length=30,null=True,blank=True)



class apdb(models.Model):
    Name=models.CharField(max_length=30,null=True,blank=True)
    Categoryname=models.CharField(max_length=30,null=True,blank=True)
    Price=models.IntegerField(null=True,blank=True)
    Author=models.CharField(max_length=30,null=True,blank=True)
    AuthorLink=models.CharField(max_length=30,null=True,blank=True)
    Publisher=models.CharField(max_length=30,null=True,blank=True)
    Date=models.DateTimeField(null=True,blank=True)
    Genres=models.CharField(max_length=30,null=True,blank=True)
    Language=models.CharField(max_length=30,null=True,blank=True)
    Page=models.IntegerField(null=True,blank=True)
    Rating=models.FloatField(null=True,blank=True)
    About=models.CharField(max_length=30,null=True,blank=True)
    Imagee=models.ImageField(upload_to="profile",null=True,blank=True)
    Pdf=models.FileField(upload_to="document",null=True,blank=True)
