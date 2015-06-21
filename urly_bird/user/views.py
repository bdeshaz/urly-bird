from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages

from user.forms import UserForm

# Create your views here.

def show_user(request, user_id):
    user = User.objects.get(id=user_id)
    bookmarks = user.update_set.all()
    return render(request,
                  "bookmarker/user.html",
                  {"user": user,
                   "bookmarks": bookmarks})


@login_required
def edit_profile(request):
    profile = get_profile(request.user)

    if request.method == "GET":
        profile_form = ProfileForm(instance=profile)
    elif request.method == "POST":
        profile_form = ProfileForm(instance=profile, data=request.POST)
        if profile_form.is_valid():
            profile_form.save()
            messages.add_message(request, messages.SUCCESS,
                                 "Your profile has been updated.")

    return render(request, "user/edit_profile.html", {"form": profile_form})


def user_register(request):
    if request.method == "GET":
        user_form = UserForm()
    elif request.method == "POST":
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.save()

            password = user.password
            # The form doesn't know to call this special method on user.
            user.set_password(password)
            user.save()

            # You must call authenticate before login. :(
            user = authenticate(username=user.username,
                                password=password)
            login(request, user)
            messages.add_message(
                request,
                messages.SUCCESS,
                "Congratulations, {}, on creating your new account! You are now logged in.".format(
                    user.username))
            return redirect('index')
    return render(request, "user/register.html", {'user_form': user_form,
                                                   })
