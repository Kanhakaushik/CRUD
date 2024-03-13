from django.db import models


class DataStore(models.Model):
    First_Name=models.CharField(max_length=200)
    # Last_Name=models.CharField(max_length=200)
    Email=models.EmailField()
    Contact=models.IntegerField()
    City=models.CharField(max_length=200)
    Password=models.CharField(max_length=200)

class QueryStore(models.Model):
    Query=models.CharField(max_length=200)
    Email=models.EmailField()
    # OrdefrId=models.CharField(max_length=200,null=True)
    

    

