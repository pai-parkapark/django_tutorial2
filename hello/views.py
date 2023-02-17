from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Post
from .forms import PostForm, UploadForm
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage, default_storage



def say_hello(request):
    print("hello")
    return HttpResponse("hello")


def post_list(requset):
    posts = Post.objects.all().order_by('created_date')
    return render(requset, 'hello/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'hello/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('hello:post_detail', pk=post.pk)

    elif request.method == "GET":
        form = PostForm()
    else:
        raise ValueError

    return render(request, 'hello/post_new.html', {'form': form})


@csrf_exempt
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('hello:post_detail', pk=post.pk)
    elif request.method == "GET":
        form = PostForm(instance=post)
    else:
        raise ValueError

    return render(request, 'hello/post_edit.html', {'form': form})


@csrf_exempt
def upload(request):
    if request.method == 'GET':
        forms = UploadForm()
        context = {'forms': forms}
        return render(request, 'hello/upload.html', context)
    elif request.method == 'POST':
        my_img = request.FILES['file']
        fs = FileSystemStorage(location='./hello/media')
        filename = fs.save(my_img.name, my_img)
        file_url = fs.url(filename)

        # my_files = request.FILES.getlist('file')
        # fs = FileSystemStorage(location='./hello/media')
        # for my_file in my_files:
        #     filename = fs.save(my_file.name, my_file)
        #     file_url = fs.url(filename)

        return HttpResponse(file_url)
