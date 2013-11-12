from django.db import models

# Create your models here.
class Ip(models.Model):
    address = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Access(models.Model):
    ip = models.ForeignKey(Ip)
    pub_date = models.DateTimeField('date published')
