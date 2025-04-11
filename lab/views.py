from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from .models import MOHArea, Sample
from .forms import MOHAreaForm, SampleForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView


def home(request):
    mohareas = MOHArea.objects.all()
    context = {"mohareas": mohareas}
    return render(request, "lab/home.html", context)


def moharea_add(request):
    """
    View to handle the creation of a new MOHArea instance.
    """
    if request.method == "POST":
        form = MOHAreaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("some_success_url")  # Replace with your success URL
    else:
        form = MOHAreaForm()
    return render(request, "lab/moharea_form.html", {"form": form})


class MOHAreaCreateView(CreateView):
    """
    View to handle the creation of a new MOHArea instance.
    Same as moharea_add
    """

    model = MOHArea
    form_class = MOHAreaForm
    template_name = "lab/moharea_form.html"
    success_url = reverse_lazy("home")


def moharea_edit(request, moharea_id):
    """
    View to handle the editing of an existing MOHArea instance.
    """
    print("Edit-Method")
    moharea = get_object_or_404(MOHArea, pk=moharea_id)
    if request.method == "POST":
        print("Post-Method")
        form = MOHAreaForm(request.POST, instance=moharea)
        if form.is_valid():
            form.save()
            return redirect("home")  # Replace with your success URL
    else:
        print("Get-Method")
        form = MOHAreaForm(instance=moharea)
    return render(request, "lab/moharea_form.html", {"form": form})


# def moharea_edit(request):
#     MOHAreaID = int(request.POST.get("MOHAreaId"))
#     mohName = request.POST.get("mohareaName")
#     moharea = MOHArea.objects.get(id=MOHAreaID)
#     moharea.name = mohName
#     moharea.save()
#     mohList = MOHArea.objects.all().order_by("name")
#     return render(request, "lab/moharea_form.html", {"mohList": mohList})


class MOHAreaUpdateView(UpdateView):
    model = MOHArea
    form_class = MOHAreaForm
    template_name = "lab/moharea_form.html"
    success_url = reverse_lazy("home")


class SampleCreateView(CreateView):
    model = Sample
    form_class = SampleForm
    template_name = "lab/moharea_form.html"
    success_url = reverse_lazy("home")


class MOHAreaListView(ListView):
    model = MOHArea
    template_name = "lab/home.html"
