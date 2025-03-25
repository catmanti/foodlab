import csv
import os
from django.core.exceptions import ObjectDoesNotExist
from lab.models import (
    PHIArea,
    MOHArea,
)  # Replace 'htmxapp' with your actual app name


def run():
    file_path = os.path.join(os.path.dirname(__file__), "phiarea.csv")

    with open(file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            try:
                moh_area = MOHArea.objects.get(id=row["MOHAreaID"])
                phiarea, created = PHIArea.objects.update_or_create(
                    name=row["PHIareas"],
                    moharea=moh_area,
                    defaults={
                        "phone": None,
                        "email": None,
                        "PHIName": None,
                    },
                )
                if created:
                    print(f"Added: {phiarea.name}")
                else:
                    print(f"Updated: {phiarea.name}")
            except ObjectDoesNotExist:
                print(f"Error: MOHArea ID {row['MOHAreaID']} not found!")
