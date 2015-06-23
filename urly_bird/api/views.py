from rest_framework import viewsets, permissions, generics
from .serializers import BookmarkSerializer
from bookmarker.models import Bookmark
from api.permissions import IsOwnerOrReadOnly


class BookmarkViewSet(viewsets.ModelViewSet):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
