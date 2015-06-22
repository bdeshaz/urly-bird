from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^(?P<s_code>[\w\-]+)$', views.show_url, name="show_url"),
    url(r'^new/', views.add_bookmark, name="add_bookmark"),
]
