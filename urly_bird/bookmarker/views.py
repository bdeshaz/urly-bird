from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404
from .models import Bookmark

def index(request):
    bookmarks = Bookmark.objects.all()

    return render(request,
                  "bookmarker/bookmarks.html",
                  bookmarks_context(request=request,
                                    bookmarks=bookmarks,
                                    header="All Bookmarks"))

def bookmarks_context(request, bookmarks, header, **kwargs):

    bookmarks = bookmarks.annotate(Count('click')).select_related()

    context = kwargs.copy()
    context.update({"header": header,
                    "bookmarks": bookmarks,
                    })

    return context