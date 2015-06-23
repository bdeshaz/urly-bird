from rest_framework import serializers
from bookmarker.models import Bookmark


class BookmarkSerializer(serializers.HyperlinkedModelSerializer):
    creator = serializers.PrimaryKeyRelatedField(read_only=True)

    _url = serializers.HyperlinkedIdentityField(view_name='api-detail')

    class Meta:
        model = Bookmark
        fields = ('id', '_url', 'url', 's_code', 'creator')
