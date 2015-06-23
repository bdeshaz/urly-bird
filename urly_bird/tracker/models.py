from django.contrib.auth.models import User
from django.db import models
from bookmarker.models import Bookmark


class Click(models.Model):
    timestamp = models.DateTimeField()
    bookmark = models.ForeignKey(
        Bookmark)  # TODO: adding related field. this allows us to be able call without using click_set
    clicker = models.ForeignKey(User, null=True)

    def __str__(self):
        return self.clicker.username
