# example of how to make seed data

import os, sys

proj_path = "/Users/briandeshazer/tiy/urly-bird/urly_bird/"
# This is so Django knows where to find stuff.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "urly_bird.settings")
sys.path.append(proj_path)

# This is so my local_settings.py gets loaded.
os.chdir(proj_path)

# This is so models get loaded.
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

from bookmarker.models import Bookmark
from tracker.models import Click

import random
from hashids import Hashids
from django.contrib.auth.models import User
from faker import Factory

fake = Factory.create()


def seed_users():
    for num in range(0, 10):
        username = fake.name()
        email = fake.free_email()
        new_user = User(username=username, email=email)
        new_user.set_password('password')
        new_user.save()


print("Seeding Users...")
seed_users()




def seed_bookmarks():
    creators = User.objects.all()

    for num in range(0, 40):
        creator = creators.get(id=(random.randint(1, len(creators)-1)))
        url = fake.url()
        hashyids = Hashids(min_length=6)
        s_code = hashyids.encode(num)
        new_bookmark = Bookmark(creator=creator, url=url, s_code=s_code)
        new_bookmark.save()


print("Seeding Bookmarks...")
seed_bookmarks()


def seed_clicks():
    bookmarks = Bookmark.objects.all()
    clickers = User.objects.all()

    for num in range(0, 100):
        random_int = random.randint(1, 39)
        print(random_int)
        bookmark = bookmarks.get(id=random_int)
        clicker = clickers.get(id=random.randint(1, len(clickers) - 1))
        timestamp = fake.date_time_this_year()
        new_click = Click(clicker=clicker, bookmark=bookmark, timestamp=timestamp)
        new_click.save()


print("Seeding Clicks...")
seed_clicks()
