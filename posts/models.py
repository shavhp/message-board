from django.db import models


# Create your models here.

# The model below is called Post
# The type of content it will hold is TextField
class Post(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:50]
