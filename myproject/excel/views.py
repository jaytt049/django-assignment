import pandas as pd
from django.shortcuts import render, redirect
from .models import UploadedFile, DataRecord
from .forms import UploadFileForm
from django.contrib.auth.decorators import login_required

@login_required
def upload_excel(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            uploaded_file = form.save(commit=False)
            uploaded_file.uploaded_by = request.user
            uploaded_file.save()

            file_path = uploaded_file.file.path

            # Read file
            if file_path.endswith('.csv'):
                df = pd.read_csv(file_path)
            else:
                df = pd.read_excel(file_path)

            # Save rows to DB
            for _, row in df.iterrows():
                try:
                    DataRecord.objects.create(
                        name=row['name'],
                        email=row['email'],
                        age=int(row['age']),
                        uploaded_file=uploaded_file
                    )
                except:
                    continue

            return redirect('data_list')
    else:
        form = UploadFileForm()

    return render(request, 'excel/upload.html', {'form': form})

@login_required
def data_list(request):
    records = DataRecord.objects.filter(uploaded_file__uploaded_by=request.user)

    return render(request, 'excel/data_list.html', {
        'records': records
    })