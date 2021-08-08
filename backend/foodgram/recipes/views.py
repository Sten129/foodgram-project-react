from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

# from .forms import PostForm, CommentForm
from django.core.paginator import Paginator
from api.models import User, Recipe, Ingredient, Follow
from .forms import RecipeForm

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
    if request.method == 'POST':
        form = RecipeForm(request.POST or None)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('index')
        #return render()
            pass

def recipe_view(request, username, recipe_id):
    recipe = get_object_or_404(Recipe, author__username=username, id=recipe_id)
    pass

def profile(request, username):
    author = get_object_or_404(User, username=username)
    all_recipes_name = author.recipes.all()
    recipes_count = all_recipes_name.count()
    paginator = Paginator(all_recipes_name, 6)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    following = request.user.is_authenticated and request.user.follower.filter(author=author).exists()
    context = {
        'page': page,
        'author': author,
        'paginator': paginator,
        'recipes_count':recipes_count,
        'following': following
    }
    return render()
    pass

@login_required
def recipe_edit(request, username, recipe_id):
    recipe = get_object_or_404(Recipe, author__username=username, id=recipe_id)
    if recipe.author != request.user:
        return redirect('recipe', username=recipe.author, recipe_id=recipe_id)
    form = RecipeForm(request.POST or None, files=request.FILES or None, instance=recipe)
    if not form.is_valid():
        return render(

        )
    form.save()
    return  redirect('recipe', username=recipe.author, recipe_id=recipe_id)
    pass

@login_required
def follow_index(request):
    pass

@login_required
def profile_follow(request, username):
    author = get_object_or_404(User, username=username)
    if author != request.user and not Follow.objects.filter(user=request.user, author=author).exists():
        Follow.objects.get_or_create(user=request.user, author=author)
    return redirect('recipe', username=username)
    pass

@login_required
def profile_unfollow(request, username):
    author = get_object_or_404(User, username=username)
    Follow.objects.filter(user=request.user, author=author).delete()
    return redirect('recipe', username=username)

    pass

@login_required
def recipe_in_favorited(request, username):
    pass

@login_required
def recipe_is_not_in_favorited(request, username):
    pass

@login_required
def recipe_is_in_shoppingcart(request, username):
    pass

@login_required
def recipe_is_out_from_shoppingcart(request, username):
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
