from django.shortcuts import render,HttpResponseRedirect
from blog.models import post
from django.contrib import messages
# Create your views here.
def blog(request):
    posts = post.objects.all()
    return render(request, 'blog_home.html', {'posts': posts})
def dashboard(request):
    user = request.user
    # print(f'''\n\n\n\n\n\n\n\n\n\n {user} \n\n\n\n\n\n\n\n {user.first_name} \n\n\n\n\n\n\n\n''')
    posts = post.objects.all()
    return render(request,'dashboard.html', {'posts': posts}, {'user':user})  
def add_post(request):
    if request.method == 'POST':
        Post = post()
        Post.title = request.POST.get('title')
        Post.desc = request.POST.get('content')
        Post.author = request.POST.get('author')
        Post.language = request.POST.get('language')
        Post.category = request.POST.get('category')
        Post.readtime = request.POST.get('readtime')

        Post.save()
        messages.success(request,'Posted successfully...')
        return HttpResponseRedirect('/blog')
    else:
        return render(request,'addpost.html')