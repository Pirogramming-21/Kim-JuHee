from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Post, IdeaStar
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.views.decorators.http import require_POST
from tools.models import Tool

# Create your views here.
def post_list(request):
    sort = request.GET.get('sort')
    if sort == 'likes':
        posts = Post.objects.annotate(star_count=Count('ideastar')).order_by('-star_count')
    elif sort == 'name':
        posts = Post.objects.all().order_by('title')
    elif sort == 'created':
        posts = Post.objects.all().order_by('created_at')
    elif sort == 'latest':
        posts = Post.objects.all().order_by('-created_at')
    else:
        posts = Post.objects.all()
    
    # 사용자가 각 포스트를 찜했는지 확인
    if request.user.is_authenticated:
        starred_posts = IdeaStar.objects.filter(user=request.user).values_list('post_id', flat=True)
    else:
        starred_posts = []
    
    context = {
        "posts": posts,
        "starred_posts": starred_posts,
    }
    return render(request, 'post_list.html', context)

@login_required
def toggle_star(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    star, created = IdeaStar.objects.get_or_create(user=request.user, post=post)

    if not created:
        star.delete()

    return JsonResponse({'starred': created})

@require_POST
def update_interest(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    action = request.POST.get('action')
    
    if action == 'increment':
        post.rating += 1
    elif action == 'decrement':
        post.rating -= 1
    post.save()
    
    return JsonResponse({'new_rating': post.rating})

def post_create(request):
    if request.method == 'POST':
        Post.objects.create(     # 폼 데이터를 받아, 새로운 'Post' 객체 생성
            title=request.POST.get("title"),
            image_url=request.POST.get("image_url"),
            review=request.POST.get("review"),
            rating=request.POST.get("rating"),
            genre=request.POST.get("genre"),
        )
        return redirect("/posts")
    return render(request, 'post_create.html')

def post_detail(request, pk):
    post = get_object_or_404(Post, id=pk)
    
    previous_post = Post.objects.filter(id__lt=pk).order_by("-id").first()
    next_post = Post.objects.filter(id__gt=pk).order_by("id").first()
    
    # 사용자가 이 포스트를 찜했는지 확인
    if request.user.is_authenticated:
        is_starred = IdeaStar.objects.filter(user=request.user, post=post).exists()
    else:
        is_starred = False
        
    print(f'post.tool: {post.tool}')  # 디버깅 로그 추가

    tool = Tool.objects.filter(name=post.tool.name).first() if post.tool else None

    print(f'tool: {tool}')  # 디버깅 로그 추가
    
    context = {
        "post": post,
        "previous_post_id": previous_post.id if previous_post else None,
        "next_post_id": next_post.id if next_post else None,
        "is_starred": is_starred,
        "tool": tool,
    }
    return render(request, 'post_detail.html', context)

def post_update(request, pk):
    post = get_object_or_404(Post, id=pk)
    if request.method == "POST":
        post.title = request.POST["title"]
        post.image_url = request.POST["image_url"]
        post.review = request.POST["review"]
        post.rating = request.POST["rating"]
        post.genre = request.POST["genre"]
        
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