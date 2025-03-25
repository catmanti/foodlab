import csv
import os
from django.core.exceptions import ObjectDoesNotExist
from lab.models import (
    FoodType,
    FoodCategory,
)  # Replace 'htmxapp' with your actual app name


def run():
    file_path = os.path.join(os.path.dirname(__file__), "FoodTypes.csv")

    with open(file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            try:
                category = FoodCategory.objects.get(id=row["CategoryID"])
                food_type, created = FoodType.objects.update_or_create(
                    name=row["SampleType"], category=category
                )

                if created:
                    print(f"Added: {food_type.name}")
                else:
                    print(f"Updated: {food_type.name}")

            except ObjectDoesNotExist:
                print(f"Error: FoodCategory ID {row['CategoryID']} not found!")
