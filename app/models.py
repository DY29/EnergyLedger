from django.db import models

# Create your models here.

class Energy(models.Model):
    provider = models.CharField( max_length=200, default = '', null = True )
    enroll_date = models.DateTimeField( blank=True,default='', null=True )


