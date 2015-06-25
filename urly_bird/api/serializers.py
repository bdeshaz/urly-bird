from django.contrib.auth.models import User
from hashids import Hashids
from rest_framework import serializers
from bookmarker.models import Bookmark
from tracker.models import Click


class ClickSerializer(serializers.ModelSerializer):
    class Meta:
        model = Click
        fields = ('bookmark', 'timestamp', 'clicker')


class BookmarkSerializer(serializers.HyperlinkedModelSerializer):
    creator = serializers.PrimaryKeyRelatedField(read_only=True)
    click_set = ClickSerializer(many=True, read_only=True)
    click_count = serializers.IntegerField(read_only=True)
    id = serializers.HyperlinkedIdentityField(view_name='bkmk')
    clicks = serializers.HyperlinkedIdentityField(view_name='user-clicks')
    s_code = serializers.CharField(read_only=True)

    def create(self, validated_data):
        hashids = Hashids(min_length=6)
        previous = Bookmark.objects.latest('id')
        previousid = previous.id
        if previous.id is None:
            previousid = 0
        bookmark = Bookmark.objects.create(**validated_data)
        bookmark.short = hashids.encrypt(previousid + 1)
        bookmark.save()
        return bookmark

    class Meta:
        model = Bookmark
        fields = (
            'id', 'url', 's_code', 'creator',
            'click_count', 'click_set', 'clicks'
        )


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
