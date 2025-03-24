import csv
import os
from django.core.exceptions import ObjectDoesNotExist
from htmxapp.models import (
    FoodParameter,
    FoodType,
    Parameter,
)  # Replace 'htmxapp' with your actual app name


def run():
    file_path = os.path.join(os.path.dirname(__file__), "Parameters.csv")

    with open(file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            try:
                food_type = FoodType.objects.get(id=row["FooDTypeID"])
                parameter = Parameter.objects.get(id=row["ParameterID"])

                food_parameter, created = FoodParameter.objects.update_or_create(
                    food_type=food_type,
                    parameter=parameter,
                    defaults={
                        "Uncertanty": row.get("Uncertanty", "").strip() or None,
                        "regulatory_limit": row.get("Regulatory Limit", "").strip()
                        or None,
                        "is_accredited": row["Accredited"].strip().upper() == "TRUE",
                        "test_method": row.get("Test Method", "").strip() or None,
                    },
                )

                if created:
                    print(
                        f"Added: {food_parameter.food_type} - {food_parameter.parameter}"
                    )
                else:
                    print(
                        f"Updated: {food_parameter.food_type} - {food_parameter.parameter}"
                    )

            except ObjectDoesNotExist:
                print(
                    f"Error: FoodType ID {row['FooDTypeID']} or Parameter ID {row['ParameterID']} not found!"
                )
