import os
import pandas as pd
import json
from django.conf import settings
from django.core.management.base import BaseCommand
from rtv_project.models import District, SubCounty, Village, Household, Survey
from etl.transformations import clean_column_names, normalize_data

DATA_PATH = os.path.join(settings.BASE_DIR, 'combined_data')
SCHEMA_PATH = os.path.join(settings.BASE_DIR, 'etl', 'schema_mapping.json')

class Command(BaseCommand):
    help = "Import and normalize household and survey data"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.NOTICE("Starting data import..."))

        # Load schema mapping
        with open(SCHEMA_PATH) as f:
            schema = json.load(f)

        # Read CSV files
        for file in os.listdir(DATA_PATH):
            if file.endswith(".csv"):
                df = pd.read_csv(os.path.join(DATA_PATH, file))
            elif file.endswith(".html"):
                df_list = pd.read_html(os.path.join(DATA_PATH, file))
                df = df_list[0]
            else:
                continue

            # Clean and map schema
            df.columns = clean_column_names(df.columns)
            df = df.rename(columns=schema.get("column_mapping", {}))

            df = normalize_data(df)

            for _, row in df.iterrows():
                # Location data
                district, _ = District.objects.get_or_create(name=row.get('district', 'Unknown'))
                subcounty, _ = SubCounty.objects.get_or_create(name=row.get('sub_county', 'Unknown'), district=district)
                village, _ = Village.objects.get_or_create(name=row.get('village', 'Unknown'), sub_county=subcounty)

                # Household data
                household, _ = Household.objects.get_or_create(
                    household_id=row.get('household_id'),
                    defaults={
                        'head_name': row.get('head_name', ''),
                        'village': village
                    }
                )

                # Survey data
                Survey.objects.update_or_create(
                    household=household,
                    survey_cycle=row.get('survey_cycle'),
                    defaults={
                        'survey_date': row.get('survey_date'),
                        'total_income': row.get('total_income'),
                        'total_expenditure': row.get('total_expenditure'),
                        'food_security_score': row.get('food_security_score'),
                        'school_enrollment': row.get('school_enrollment'),
                        'water_access': row.get('water_access'),
                        'latrine_access': row.get('latrine_access'),
                        'remarks': row.get('remarks', '')
                    }
                )

        self.stdout.write(self.style.SUCCESS("Data import completed successfully."))
