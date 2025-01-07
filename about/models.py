from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class About(models.Model):
    """
    Stores a single about page entry.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    profile_image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):  # add the magic method
        return self.title  # ensure it returns the string title of the about page


class CollaborateRequest(models.Model):
    """
    Stores a single collaboration request entry.
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration request from {self.name}"
