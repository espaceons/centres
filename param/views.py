from django.shortcuts import redirect, render

from param.forms import CentreForm
from param.models import Centre


def create_centre(request):
    if request.method == 'POST':
        form = CentreForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('param:liste')
    else:
        form = CentreForm()  # Create an empty form for GET requests
    context = {'form': form}
    return render(request, "param/create_centre.html", context)


def liste_centre(request):
    centre = Centre.objects.all()
    context = {
        'centre':centre,
    }
    
    return render(request,'param/liste_centre.html', context)

def update_centre(request, pk):
    obj = Centre.objects.get(id = pk)
    form = CentreForm(instance=obj)
    if request.method == 'POST':
        form = CentreForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('param:liste')
    template_name = 'param/create_centre.html'
    context = {'form': form}
    return render(request, template_name, context)


def delete_centre(request, pk):
    obj = Centre.objects.get(id = pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('param:liste')
    template_name = 'param/confirmation.html'
    context = {'obj': obj}
    return render(request, template_name, context)
        