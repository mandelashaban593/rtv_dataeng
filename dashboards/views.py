import os
import pandas as pd
from django.conf import settings
from django.shortcuts import render
from core.models import Household, Survey


BASELINE_CSV = os.path.join(settings.BASE_DIR, 'combined_data', '01_baseline.csv')
YEAR_ONE_CSV = os.path.join(settings.BASE_DIR, 'combined_data', '02_year_one.csv')
YEAR_TWO_CSV = os.path.join(settings.BASE_DIR, 'combined_data', '03_year_two.csv')


def clean_and_standardize(df, year):
    df = df.copy()
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    df["survey_year"] = year
    if 'income' in df.columns:
        df['income'] = pd.to_numeric(df['income'], errors='coerce')
    return df


def load_and_process_csvs():
    dataframes = []

    if os.path.exists(BASELINE_CSV):
        df_base = pd.read_csv(BASELINE_CSV)
        df_base = clean_and_standardize(df_base, "baseline")
        dataframes.append(df_base)

    if os.path.exists(YEAR_ONE_CSV):
        df_y1 = pd.read_csv(YEAR_ONE_CSV)
        df_y1 = clean_and_standardize(df_y1, "year_one")
        dataframes.append(df_y1)

    if os.path.exists(YEAR_TWO_CSV):
        df_y2 = pd.read_csv(YEAR_TWO_CSV)
        df_y2 = clean_and_standardize(df_y2, "year_two")
        dataframes.append(df_y2)

    if not dataframes:
        # Return empty dataframe with expected columns if no CSVs found
        return pd.DataFrame(columns=["household_id", "income", "location", "survey_year"])

    return pd.concat(dataframes, ignore_index=True)


def persist_to_database(df):
    for _, row in df.iterrows():
        household_id = row.get('household_id')
        if not household_id:
            continue  # skip rows without household_id

        household, _ = Household.objects.get_or_create(household_id=household_id)
        Survey.objects.update_or_create(
            household=household,
            survey_year=row.get('survey_year'),
            defaults={
                'income': row.get('income'),
                'location': row.get('location', 'Unknown'),
            }
        )


def dashboard_view(request):
    # Load and process CSVs
    df_all = load_and_process_csvs()

    # Persist data only if df_all is not empty
    if not df_all.empty:
        persist_to_database(df_all)

    # Calculate metrics: mean income per survey year (will be empty if no data)
    metrics = df_all.groupby('survey_year')['income'].mean().reset_index()

    # Render the dashboard template with metrics data
    return render(request, 'dashboards/dashboard_embed.html', {
        'metrics': metrics.to_dict(orient='records')
    })
