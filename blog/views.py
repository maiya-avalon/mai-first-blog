from django.shortcuts import render
from django.utils import timezone 
from .models import BlogPost

# Create your views here. create a function (def) called post_list that takes request and will return the value it gets from calling function render
def post_list(request):
    posts = BlogPost.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
