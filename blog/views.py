from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
# Create your views here.

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {"posts": posts})

def post_detail(request, pk):
	# post_detail = Post.objects.get(pk=pk)
	post_detail = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {"post_detail": post_detail})