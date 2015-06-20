from django.contrib.auth.models import User
from django.db import models
from bookmarker.models import Bookmark


class Click(models.Model):
    timestamp = models.DateTimeField()
    bookmark = models.ForeignKey(Bookmark)
    clicker = models.ForeignKey(User, null=True)