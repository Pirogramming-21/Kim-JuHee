from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    context = {
        "posts": posts
    }
    return render(request, 'post_list.html', context)

def post_create(request):
    if request.method == 'POST':
        Post.objects.create(     # 폼 데이터를 받아, 새로운 'Post' 객체 생성
            title=request.POST.get("title"),
            year=request.POST.get("year"),
            genre=request.POST.get("genre"),
            rating=request.POST.get("rating"),
            runtime=request.POST.get("runtime"),
            review=request.POST.get("review"),
            director=request.POST.get("director"),
            actors=request.POST.get("actors"),
            image_url=request.POST.get("image_url")
        )
        return redirect("/posts")
    return render(request, 'post_create.html')

def post_detail(request, pk):
    post = get_object_or_404(Post, id=pk)
    
    previous_post = Post.objects.filter(id__lt=pk).order_by("-id").first()
    next_post = Post.objects.filter(id__gt=pk).order_by("id").first()
    
    context = {
        "post": post,
        "previous_post_id": previous_post.pk if previous_post else None,
        "next_post_id": next_post.pk if next_post else None
    }
    return render(request, 'post_detail.html', context)

def post_update(request, pk):
    post = get_object_or_404(Post, id=pk)
    if request.method == "POST":
        post.title = request.POST["title"]
        post.year = request.POST["year"]
        post.genre = request.POST["genre"]
        post.rating = request.POST["rating"]
        post.runtime = request.POST["runtime"]
        post.review = request.POST["review"]
        post.director = request.POST["director"]
        post.actors = request.POST["actors"]
        post.image_url = request.POST["image_url"]
        
        post.save()
        
        return redirect(f"/posts/{pk}")
    
    context = {
        "post": post
    }
    return render(request, 'post_update.html', context)

def post_delete(request, pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=pk)
        post.delete()
        return redirect("/posts")
    return HttpResponse("Invalid request method.", status=405)