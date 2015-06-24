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

    click_info = serializers.HyperlinkedIdentityField(view_name='click-detail')

    class Meta:
        model = Bookmark
        fields = (
            'id', 'click_info', 'url', 's_code', 'creator',
            'click_count', 'click_set', 'clicks'
        )
