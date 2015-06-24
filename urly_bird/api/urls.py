from django.conf.urls import url, include
from rest_framework import routers
from . import views
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'bookmarks', views.BookmarkViewSet, base_name="bookmark")

urlpatterns = [
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^clicks/$', views.ClickCreateView.as_view()),
    url(r'^clicks/(?P<pk>\d+)$', views.ClickDetailView.as_view(), name="click-detail"),
]
