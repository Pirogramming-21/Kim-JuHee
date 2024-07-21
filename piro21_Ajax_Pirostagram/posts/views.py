import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Post, Comment

def post_list(request):
    posts = Post.objects.all()
    context = {
        "posts": posts
    }
    return render(request, 'post_list.html', context)

def post_create(request):
    if request.method == 'POST':    
        Post.objects.create(  
            title=request.POST.get("title"),
            user=request.POST.get("user"),
            content=request.POST.get("content"),
            image_url=request.POST.get("image_url")
        )
        return redirect("/posts/")
    return render(request, 'post_create.html')

def post_detail(request, pk):
    post = get_object_or_404(Post, id=pk)
    comments = Comment.objects.filter(post=post)
    
    previous_post = Post.objects.filter(id__lt=pk).order_by("-id").first()
    next_post = Post.objects.filter(id__gt=pk).order_by("id").first()
    
    context = {
        "post": post,
        "previous_post_id": previous_post.pk if previous_post else None,
        "next_post_id": next_post.pk if next_post else None,
        'comments': comments
    }
    return render(request, 'post_detail.html', context)

def post_update(request, pk):
    post = get_object_or_404(Post, id=pk)
    if request.method == "POST":
        post.title = request.POST["title"]
        post.user = request.POST["user"]
        post.content = request.POST["content"]
        post.image_url = request.POST["image_url"]
        
        post.save()
        
        return redirect(f"/posts/{pk}/")
    
    context = {
        "post": post
    }
    return render(request, 'post_update.html', context)

def post_delete(request, pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=pk)
        post.delete()
    return redirect("/posts/")

def comment_create(request, pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=pk)
        data = json.loads(request.body)
        comment = Comment.objects.create(
            post=post,
            content=data['content']
        )
        return JsonResponse({'success': True, 'comment': {'id': comment.id, 'content': comment.content, 'post': post.id}})
    return JsonResponse({'success': False}, status=400)

@csrf_exempt
def comment_delete(request, post_pk, comment_pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=post_pk)
        comment = get_object_or_404(Comment, id=comment_pk, post=post)
        comment.delete()
        return JsonResponse({'success': True, 'comment': {'id': comment_pk}})
    return JsonResponse({'success': False}, status=400)
        


@csrf_exempt
def like_ajax(request):
    if request.method == 'POST':
        req = json.loads(request.body)
        post_id = req['id']
        button_type = req['type']
        
        post = Post.objects.get(id=post_id)
        
        if button_type == 'like':
            post.like += 1
            post.save()
        
        return JsonResponse({'id': post_id, 'type': button_type})
    return JsonResponse({'error': 'Invalid request'}, status=400)
