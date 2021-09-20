import os
import csv
from django.core.management.base import BaseCommand

from restaurant.models import Restaurant

class Command(BaseCommand):
    help = "Loads restaurant data from .csv to app model"

    def handle(self, *args, **options):
        def preprocess_value(value, field_name):
            if field_name in ["lat", "lng"]:
                return float(value)
            elif field_name in ["rating"]:
                return int(value)
            else:
                return str(value)

        print("Attemping to load restaurant data: ", end="")
        csv_path = os.path.join(
            os.getcwd(),
            "backend/apps/restaurant/data/restaurantes.csv"
        )
        print(csv_path)
        header_read = False
        with open(csv_path) as f:
            reader = csv.reader(f)
            for row in reader:
                if not header_read:
                    fields = row
                    header_read = True
                    continue
                
                _, created = Restaurant.objects.get_or_create(**{
                    field_name: preprocess_value(value, field_name) for field_name, value in zip(fields, row)
                    })
        print("> Restaurant data loaded")