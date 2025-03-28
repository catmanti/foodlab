from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from .models import MOHArea, Sample
from .forms import MOHAreaForm, SampleForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView


def home(request):
    return render(request, "lab/home.html", {"count": range(15)})


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
    moharea = get_object_or_404(MOHArea, pk=moharea_id)
    if request.method == "POST":
        form = MOHAreaForm(request.POST, instance=moharea)
        if form.is_valid():
            form.save()
            return redirect("home")  # Replace with your success URL
    else:
        form = MOHAreaForm(instance=moharea)
    return render(request, "lab/moharea_form.html", {"form": form})


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
