from rest_framework import viewsets, permissions, generics
from .serializers import BookmarkSerializer, ClickSerializer
from bookmarker.models import Bookmark
from api.permissions import IsOwnerOrReadOnly, OwnsRelatedClick
from tracker.models import Click


class BookmarkViewSet(viewsets.ModelViewSet):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class ClickCreateView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,
                          OwnsRelatedClick)
    serializer_class = ClickSerializer

    def perform_create(self, serializer):
        click = serializer.validated_data['click']
        if self.request.user != click.clicker:
            raise PermissionError
        serializer.save()

class ClickDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,
                          OwnsRelatedClick)
    serializer_class = ClickSerializer
    queryset = Click.objects.all()

