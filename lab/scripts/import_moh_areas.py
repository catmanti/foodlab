import csv
import os
from django.core.exceptions import ObjectDoesNotExist
from htmxapp.models import (
    MOHArea,
    District,
)  # Replace 'yourapp' with your actual app name


def run():
    file_path = os.path.join(os.path.dirname(__file__), "moh_areas.csv")

    with open(file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            try:
                district = District.objects.get(id=row["districtID"])
                moh_area, created = MOHArea.objects.update_or_create(
                    name=row["Name"],
                    district=district,
                    defaults={
                        "address": row.get("address", ""),
                        "phone": None,
                        "email": None,
                    },
                )
                if created:
                    print(f"Added: {moh_area.name}")
                else:
                    print(f"Updated: {moh_area.name}")
            except ObjectDoesNotExist:
                print(f"Error: District ID {row['districtID']} not found!")
