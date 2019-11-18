from django.db import models

# Create your models here.
class festival(models.Model):
  name = models.CharField(max_length="30", default="")
  # starttime = models.DateTimeField(auto_add_now=False, )
  place = models.CharField(max_length="30", default="")
  price = models.IntegerField(default="", null=True)
  lineup = models.TextField(default="")
  # post = models.ImageField()
  