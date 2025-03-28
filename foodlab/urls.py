"""
URL configuration for foodlab project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from lab.views import (
    moharea_add,
    moharea_edit,
    home,
    MOHAreaCreateView,
    MOHAreaUpdateView,
    SampleCreateView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("moharea/add/", moharea_add, name="moharea_add"),
    path("moharea/create/", MOHAreaCreateView.as_view(), name="moharea_create"),
    path("moharea/edit/<int:moharea_id>/", moharea_edit, name="moharea_edit"),
    path(
        "moharea/update/<int:pk>/",
        MOHAreaUpdateView.as_view(),
        name="moharea_update",
    ),
    path("sample/create/", SampleCreateView.as_view(), name="sample_create"),
]
