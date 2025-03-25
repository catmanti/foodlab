from django.contrib import admin
from .models import (
    District,
    MOHArea,
    PHIArea,
    FoodCategory,
    FoodType,
    Parameter,
    FoodParameter,
    Sample,
    StaffMember,
)

admin.site.register(District)
admin.site.register(MOHArea)
admin.site.register(PHIArea)
admin.site.register(FoodCategory)
admin.site.register(FoodType)
admin.site.register(Parameter)
admin.site.register(FoodParameter)
admin.site.register(Sample)
admin.site.register(StaffMember)
