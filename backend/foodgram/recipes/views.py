from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

# from .forms import PostForm, CommentForm
from django.core.paginator import Paginator
from .models import User, Recipe, Ingredient, Follow

# Create your views here.
def index(requst):
    recipe_list = Recipe.objects.all()
    paginator = Paginator(recipe_list, 6)
    page_nubmer = requst.GET.get('page')
    page = paginator.get_page(page_nubmer)
    return render()
    pass

@login_required
def new_recipe(request):
    pass

def recipe_view(request, username, recipe_id):
    pass

def profile(request, username):
    pass

@login_required
def recipe_edit(request, username, recipe_id):
    pass

@login_required
def follow_index(request):
    pass

@login_required
def profile_follow(request, username):
    pass

@login_required
def profile_unfollow(request, username):
    pass

def page_not_found(request, exception):  # noqa
    return render(
        request,
        "misc/404.html",
        {"path": request.path},
        status=404
    )


def server_error(request):
    return render(request, "misc/500.html", status=500)
