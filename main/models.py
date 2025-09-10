import uuid
from django.db import models

class News(models.Model):
    CATEGORY_CHOICES = [
        ('sepakbola', 'Sepakbola'),
        ('basket', 'Basket'),
        ('voli', 'Voli'),
        ('padel', 'Padel'),
        ('lari', 'Lari'),
        ('bulutangkis', 'Bulutangkis'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update')
    thumbnail = models.URLField(blank=True, null=True)
    product_views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
    @property
    def is_news_hot(self):
        return self.news_views > 20
        
    def increment_views(self):
        self.news_views += 1
        self.save()
