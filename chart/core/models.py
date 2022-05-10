from tabnanny import verbose
from django.db import models

# Create your models here.

class Post(models.Model):
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Postlar"
    title = models.CharField(max_length=100)
    daromadi = models.IntegerField()
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
