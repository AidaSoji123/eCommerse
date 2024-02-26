from django.db import models

class Product(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = ((LIVE, 'live'), (DELETE, 'delete'))
    
    title = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='products/images/')  # Updated upload_to parameter
    priority = models.IntegerField(default=0)  # Consider adding a comment to explain the purpose of this field
    delete_status = models.IntegerField(choices=DELETE_CHOICES, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.title
