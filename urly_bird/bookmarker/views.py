from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from hashids import Hashids
from .models import Bookmark
from .forms import BookmarkForm


def index(request):
    bookmarks = Bookmark.objects.all()

    return render(request,
                  "bookmarker/bookmarks.html",
                  bookmarks_context(request=request,
                                    bookmarks=bookmarks,
                                    header="All Bookmarks"))


def bookmarks_context(request, bookmarks, header, **kwargs):
    page = request.GET.get('page', 1)
    per_page = request.GET.get('per_page', 20)

    bookmarks = bookmarks.annotate(Count('clicks')).select_related()
    bookmarks_paginator = Paginator(bookmarks, per_page)

    context = kwargs.copy()
    context.update({"header": header,
                    "bookmarks": bookmarks_paginator.page(page),
                    })

    return context


def show_url(request, s_code):
    bookmark = Bookmark.objects.get(s_code=s_code)
    return HttpResponseRedirect(redirect_to=bookmark.url)


def add_bookmark(request):
    num = Bookmark.objects.count()  # TODO link to natural id
    if request.method == "POST":
        form = BookmarkForm(request.POST)
        if form.is_valid():
            bookmark = form.save(commit=False)
            bookmark.creator = request.user
            hashyids = Hashids(min_length=6)
            bookmark.s_code = hashyids.encode(num)
            bookmark.save()
            messages.add_message(request, messages.SUCCESS,
                                 "Bookmark created!")
            return redirect("index")
    else:
        form = BookmarkForm()

    return render(request, "bookmarker/add.html", {"form": form})
