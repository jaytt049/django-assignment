from django.shortcuts import render, redirect, get_object_or_404
from .models import Lead
from .forms import LeadForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required

@login_required
def lead_list(request):
    query = request.GET.get('q')
    status = request.GET.get('status')

    leads = Lead.objects.filter(created_by=request.user)

    if query:
        leads = leads.filter(
            Q(name__icontains=query) |
            Q(email__icontains=query)
        )

    if status:
        leads = leads.filter(status=status)

    return render(request, 'leads/lead_list.html', {
        'leads': leads
    })

@login_required
def add_lead(request):
    if request.method == 'POST':
        form = LeadForm(request.POST)

        if form.is_valid():
            lead = form.save(commit=False)
            lead.created_by = request.user
            lead.save()
            return redirect('lead_list')
    else:
        form = LeadForm()

    return render(request, 'leads/add_lead.html', {'form': form})

@login_required
def edit_lead(request, id):
    lead = get_object_or_404(Lead, id=id, created_by=request.user)

    form = LeadForm(request.POST or None, instance=lead)

    if form.is_valid():
        form.save()
        return redirect('lead_list')

    return render(request, 'leads/edit_lead.html', {'form': form})

@login_required
def delete_lead(request, id):
    lead = get_object_or_404(Lead, id=id, created_by=request.user)
    lead.delete()
    return redirect('lead_list')