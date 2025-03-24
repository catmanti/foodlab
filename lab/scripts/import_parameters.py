import csv
import os
from htmxapp.models import Parameter  # Replace 'htmxapp' with your actual app name


def run():
    file_path = os.path.join(os.path.dirname(__file__), "ParameterTypes.csv")

    with open(file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            parameter_name = row["ParameterName"].strip()
            unit_type = row["unitType"].strip()

            parameter, created = Parameter.objects.update_or_create(
                name=parameter_name, defaults={"unit_type": unit_type}
            )

            if created:
                print(f"Added: {parameter.name}")
            else:
                print(f"Updated: {parameter.name}")
