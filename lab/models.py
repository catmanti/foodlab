from django.db import models
from django.utils.translation import gettext_lazy as _


class District(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class MOHArea(models.Model):
    name = models.CharField(max_length=50)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=20, null=True)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.name


class PHIArea(models.Model):
    name = models.CharField(max_length=50)
    moharea = models.ForeignKey(MOHArea, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, null=True)
    email = models.EmailField(null=True)
    PHIName = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


class FoodCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class FoodType(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Parameter(models.Model):
    name = models.CharField(max_length=50)
    unit_type = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class StaffMember(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True)
    currently_active = models.BooleanField(default=True)
    role = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


class FoodParameter(models.Model):
    parameter = models.ForeignKey(Parameter, on_delete=models.CASCADE)
    food_type = models.ForeignKey(FoodType, on_delete=models.CASCADE)
    Uncertanty = models.CharField(max_length=50, null=True)
    regulatory_limit = models.CharField(max_length=50, null=True)
    is_accredited = models.BooleanField(default=False)
    test_method = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f"{self.food_type} - {self.parameter}  "


class Sample(models.Model):
    sampleid = models.CharField(max_length=12, unique=True)
    foodtype = models.ForeignKey(FoodType, on_delete=models.CASCADE)
    MOHArea = models.ForeignKey(
        MOHArea,
        on_delete=models.CASCADE,
    )
    PHIArea = models.ForeignKey(
        PHIArea,
        on_delete=models.CASCADE,
    )
    date_collected = models.DateField()
    analysis_by = models.ForeignKey(StaffMember, on_delete=models.CASCADE)
