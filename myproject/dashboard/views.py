from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from blog.models import Blog
from leads.models import Lead
from files.models import File
from excel.models import DataRecord

@login_required
def dashboard(request):
    user = request.user

    if user.is_superuser:
        context = {
            'total_users': User.objects.count(),
            'total_blogs': Blog.objects.count(),
            'total_leads': Lead.objects.count(),
            'total_files': File.objects.count(),
            'total_records': DataRecord.objects.count(),
            'is_admin': True
        }
    else:
        context = {
            'total_blogs': Blog.objects.filter(user=user).count(),
            'total_leads': Lead.objects.filter(created_by=user).count(),
            'total_files': File.objects.filter(uploaded_by=user).count(),
            'total_records': DataRecord.objects.filter(
                uploaded_file__uploaded_by=user
            ).count(),
            'is_admin': False
        }

    return render(request, 'dashboard.html', context)