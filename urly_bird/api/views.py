from django.db.models import Count
from rest_framework import viewsets, permissions, generics, filters
from .serializers import BookmarkSerializer, ClickSerializer
from bookmarker.models import Bookmark
from api.permissions import IsOwnerOrReadOnly, OwnsRelatedClick
from tracker.models import Click
import django_filters


class BookmarkFilter(django_filters.FilterSet):
    creator = django_filters.CharFilter(name="creator", lookup_type="icontains")
    s_code = django_filters.CharFilter(name="s_code", lookup_type="icontains")

    class Meta:
        model = Bookmark
        fields = ['creator', 's_code']


class BookmarkViewSet(viewsets.ModelViewSet):
    # queryset = Bookmark.objects.all()
    queryset = Bookmark.objects.annotate(
        click_count=Count('clicks', distinct=True)
    )

    serializer_class = BookmarkSerializer
    permission_classes = (permissions.IsAuthenticated,
                          IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def get_queryset(self):
        return Bookmark.objects.filter(creator=self.request.user).annotate(
            click_count=Count('clicks', distinct=True)
        )

    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = BookmarkFilter


class ClickCreateView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,
                          OwnsRelatedClick)
    serializer_class = ClickSerializer

    def perform_create(self, serializer):
        click = serializer.validated_data['click']
        if self.request.user != click.clicker:
            raise PermissionError
        serializer.save()


class ClickDetailView(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,
                          )
    serializer_class = ClickSerializer
    queryset = Click.objects.all()

    # def get_queryset(self):
    #     return Click.objects.filter(clicker=self.request.user)
    #  FIXME: so the above is only trying to show clicks that have been made
    #  FIXME: by that user
