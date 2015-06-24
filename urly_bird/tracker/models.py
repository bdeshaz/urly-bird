from django.contrib.auth.models import User
from django.db import models
from bookmarker.models import Bookmark


class Click(models.Model):
    timestamp = models.DateTimeField()
    bookmark = models.ForeignKey(Bookmark, related_name="clicks")
    clicker = models.ForeignKey(User, null=True)

    def __str__(self):
        return self.clicker.username
