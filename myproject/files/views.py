from django.shortcuts import render, redirect
from .models import File
from .forms import FileForm
from django.contrib.auth.decorators import login_required

@login_required
def file_list(request):
    category = request.GET.get('category')

    files = File.objects.filter(uploaded_by=request.user)

    if category:
        files = files.filter(category__id=category)

    return render(request, 'files/file_list.html', {
        'files': files
    })

@login_required
def upload_file(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)

        if form.is_valid():
            file = form.save(commit=False)
            file.uploaded_by = request.user
            file.save()
            return redirect('file_list')
    else:
        form = FileForm()

    return render(request, 'files/upload_file.html', {'form': form})