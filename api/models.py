from django.db import models

# Create your models here.
class Director(models.Model):
    name = models.CharField(max_length=60)
    surname = models.CharField(max_length=60)
    def __str__(self):
        return self.name+" "+ self.surname
class Movies(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField(default=2000)
    director = models.ForeignKey(Director,on_delete=models.PROTECT,blank=True,null=True)
    
    def __str__(self):
        return self.title



