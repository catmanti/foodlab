import csv
import os
from htmxapp.models import FoodCategory  # Replace 'htmxapp' with your actual app name


def run():
    file_path = os.path.join(os.path.dirname(__file__), "Categories.csv")

    with open(file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            category_name = row["FoodCategory"].strip()

            food_category, created = FoodCategory.objects.update_or_create(
                name=category_name
            )

            if created:
                print(f"Added: {food_category.name}")
            else:
                print(f"Updated: {food_category.name}")
