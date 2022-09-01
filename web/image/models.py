from django.db import models
# Create your models here.
class Image(models.Model):
    file = models.ImageField()
    uploaded_at =  models.DateTimeField(auto_now_add=True)
    def __str__(self):
        self.file