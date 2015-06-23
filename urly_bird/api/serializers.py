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

    _url = serializers.HyperlinkedIdentityField(view_name='bookmark-detail')

    class Meta:
        model = Bookmark
        fields = ('id', '_url', 'url', 's_code', 'creator', 'click_set')
