from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, Category, Tag
from .forms import BlogForm, RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
import csv
from io import TextIOWrapper
from .forms import CSVUploadForm
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Blog
from .serializers import BlogSerializer

@login_required
def upload_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)

        if form.is_valid():
            file = request.FILES['file']

            csv_file = TextIOWrapper(file.file, encoding='utf-8')
            reader = csv.DictReader(csv_file)

            for row in reader:
                Blog.objects.create(
                    title=row['title'],
                    description=row['description'],
                    user=request.user,
                    category=Category.objects.first()
                )

            return redirect('blog_list')

    else:
        form = CSVUploadForm()

    return render(request, 'blog/upload_csv.html', {'form': form})

def blog_list(request):
    query = request.GET.get('q')
    category_id = request.GET.get('category')

    blogs = Blog.objects.all()

    if query:
        blogs = blogs.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )

    if category_id:
        blogs = blogs.filter(category_id=category_id)

    paginator = Paginator(blogs, 3)
    page_number = request.GET.get('page')
    blogs = paginator.get_page(page_number)

    categories = Category.objects.all()

    return render(request, 'blog/blog_list.html', {
        'blogs': blogs,
        'categories': categories,
        'query': query,
        'selected_category': category_id
    })

@login_required
def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)

        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.user
            blog.save()

            form.save_m2m()

            return redirect('blog_list')
    else:
        form = BlogForm()

    return render(request, 'blog/add_blog.html', {'form': form})

@login_required
def edit_blog(request, id):
    blog = get_object_or_404(Blog, id=id)

    if blog.user != request.user:
        messages.error(request, "You are not allowed to edit this post")
        return redirect('blog_list')

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, "Blog updated")
            return redirect('blog_list')
    else:
        form = BlogForm(instance=blog)

    return render(request, 'blog/edit_blog.html', {'form': form})

@login_required
def delete_blog(request, id):
    blog = get_object_or_404(Blog, id=id)

    if blog.user != request.user:
        messages.error(request, "You are not allowed to delete this post")
        return redirect('blog_list')

    blog.delete()
    messages.success(request, "Blog deleted successfully")
    return redirect('blog_list')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()

            send_mail(
                subject='Welcome 🎉',
                message='Welcome!',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email],
                html_message='<h1>Welcome to Blog App 🚀</h1>'
            )

            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'blog/register.html', {'form': form})

@api_view(['GET'])
def api_blog_list(request):
    blogs = Blog.objects.all()
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def api_add_blog(request):
    serializer = BlogSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors)