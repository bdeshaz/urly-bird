from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Bookmark(models.Model):
    url = models.URLField(max_length=200)
    s_code = models.CharField(max_length=200, unique=True)
    creator = models.ForeignKey(User, related_name="bookmarks")

    def __str__(self):
        return self.s_code





