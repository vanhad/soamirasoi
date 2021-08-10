from django.db import models

# Create your models here.
class Food(models.Model):
    ItemName = models.CharField(max_length=50)
    ItemCat = models.CharField(max_length=15)
    ItemDesc = models.TextField()
    ItemPrice = models.IntegerField()
    ItemImage = models.ImageField(upload_to='pics')
    def __str__(self):
        return self.ItemName
    
class Contact(models.Model):
    Name = models.CharField(max_length=15)
    Email = models.EmailField()
    Message = models.TextField()
    def __str__(self):
        return self.Name