import os
import pandas as pd
from django.conf import settings
from django.shortcuts import render
from core.models import Household, Survey
from django.contrib.auth.decorators import login_required


# Define CSV paths
BASELINE_CSV = os.path.join(settings.BASE_DIR, 'combined_data', '01_baseline.csv')
YEAR_ONE_CSV = os.path.join(settings.BASE_DIR, 'combined_data', '02_year_one.csv')
YEAR_TWO_CSV = os.path.join(settings.BASE_DIR, 'combined_data', '03_year_two.csv')


def clean_and_standardize(df, year):
    df = df.copy()

    # Standardize column names
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    # Fix duplicate column names by appending suffixes
    seen = {}
    new_columns = []
    for col in df.columns:
        if col in seen:
            seen[col] += 1
            new_columns.append(f"{col}_{seen[col]}")
        else:
            seen[col] = 0
            new_columns.append(col)
    df.columns = new_columns

    # Add survey year column
    df["survey_year"] = year

    # Convert income column to numeric if present
    if 'income' in df.columns:
        df['income'] = pd.to_numeric(df['income'], errors='coerce')

    return df


def load_and_process_csvs():
    dataframes = []

    if os.path.exists(BASELINE_CSV):
        df_base = pd.read_csv(BASELINE_CSV)
        print("Baseline CSV data (raw):", df_base.head())
        df_base = clean_and_standardize(df_base, "baseline")
        print("Cleaned Baseline CSV data:", df_base.head())
        dataframes.append(df_base)

    if os.path.exists(YEAR_ONE_CSV):
        df_y1 = pd.read_csv(YEAR_ONE_CSV)
        print("Year One CSV data (raw):", df_y1.head())
        df_y1 = clean_and_standardize(df_y1, "year_one")
        print("Cleaned Year One CSV data:", df_y1.head())
        dataframes.append(df_y1)

    if os.path.exists(YEAR_TWO_CSV):
        df_y2 = pd.read_csv(YEAR_TWO_CSV)
        print("Year Two CSV data (raw):", df_y2.head())
        df_y2 = clean_and_standardize(df_y2, "year_two")
        print("Cleaned Year Two CSV data:", df_y2.head())
        dataframes.append(df_y2)

    if not dataframes:
        print("⚠️ No dataframes loaded. Returning empty DataFrame.")
        return pd.DataFrame(columns=["household_id", "income", "location", "survey_year"])

    try:
        return pd.concat(dataframes, ignore_index=True)
    except pd.errors.InvalidIndexError as e:
        print(f"🚨 Error during concatenation: {e}")
        for i, df in enumerate(dataframes):
            print(f"DataFrame {i} columns: {df.columns.tolist()}")
        raise


def persist_to_database(df):
    for _, row in df.iterrows():
        household_id = row.get('household_id')
        if not household_id:
            continue  # Skip rows without household_id

        household, _ = Household.objects.get_or_create(household_id=household_id)
        Survey.objects.update_or_create(
            household=household,
            survey_year=row.get('survey_year'),
            defaults={
                'income': row.get('income'),
                'location': row.get('location', 'Unknown'),
            }
        )


@login_required
def dashboard_view(request):
    # Load and process CSVs
    df_all = load_and_process_csvs()

    if df_all.empty:
        return render(request, 'dashboards/dashboard_embed.html', {
            'metrics': [],
            'error': 'No data available.'
        })

    # Determine correct column name for income
    possible_income_columns = [col for col in df_all.columns if 'income' in col]
    print("Available income-like columns:", possible_income_columns)

    # Pick most likely income column
    income_col = None
    for col in possible_income_columns:
        if 'hh_income' in col or 'usd' in col:
            income_col = col
            break

    if not income_col:
        return render(request, 'dashboards/dashboard_embed.html', {
            'metrics': [],
            'error': "Could not find income column in data."
        })

    df_all[income_col] = pd.to_numeric(df_all[income_col], errors='coerce')

    # Group and summarize income
    metrics = df_all.groupby('survey_year')[income_col].mean().reset_index()
    metrics.rename(columns={income_col: 'average_income'}, inplace=True)

    # Render dashboard
    return render(request, 'dashboards/dashboard_embed.html', {
        'metrics': metrics.to_dict(orient='records')
    })
