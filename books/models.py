from django.db import models
from django.urls import reverse
import uuid
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from accounts.models import CustomUser

User = get_user_model()

class Book(models.Model):
    id = models.UUIDField(primary_key=True, 
                          # db_index=True,
                          default=uuid.uuid4, 
                          editable=False)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.ImageField(upload_to='covers/', blank=True) 
    
    class Meta:
        # no need to migrate 
        indexes = [
            models.Index(fields=['id'],name="id_index"),
        ]
        
        permissions = [
            ("special_status", "Can read all books"),
        ]
    
    def __str__(self):
        return self.title
    
    # def get_absolute_url(self):
    #     return reverse("book_detail", args=[str(self.id)])
    
    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"pk": self.pk})
    
    
class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews',)
    review = models.CharField(max_length=255)
    author = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE,)
    
    def __str__(self):
        return self.review    
    
    
