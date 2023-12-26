from django.shortcuts import render, redirect, get_object_or_404
from .forms import ToursForm, CountriesForm
from .models import Countries, Tours

def tours_add(request):
    if request.method == 'POST':
        tour = ToursForm(request.POST)
        if tour.is_valid():
            tour.save()
            return redirect('index')
    else:
        tour = ToursForm()
    return render(request, 'app/tours_form.html', {'tour': tour})

def tours_list(request):
    tour = Tours.objects.all()
    return render(request, 'app/index.html', {'tour': tour})

def tours_detail(request, pk):
    tour = get_object_or_404(Tours, pk=pk)
    return render(request, 'app/tours_detail.html', {'tour': tour})

def tours_edit(request, pk):
    tour = get_object_or_404(Tours, pk=pk)
    if request.method == 'POST':
        tour = ToursForm(request.POST, instance=tour)
        if tour.is_valid():
            tour.save()
            return redirect('index')
    else:
        tour = ToursForm(instance=tour)
    return render(request, 'app/tours_form.html', {'tour': tour})

def tours_delete(request, pk):
    tour = get_object_or_404(Tours, pk=pk)
    tour.delete()
    return redirect('index')
