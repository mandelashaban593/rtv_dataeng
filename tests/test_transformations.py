# tests/test_transformations.py
import unittest
import pandas as pd
from etl.transformations import (
    clean_missing_values,
    rename_variables,
    normalize_column,
)

class TestTransformations(unittest.TestCase):

    def setUp(self):
        # Sample dataframe with missing values and inconsistent column names
        self.df = pd.DataFrame({
            'HH_ID': [1, 2, 3, 4],
            'Income_2021': [5000, None, 7000, 8000],
            'Poverty_Status': ['Poor', 'Poor', 'Not Poor', None],
        })

        # Sample schema mapping for renaming
        self.schema_map = {
            'Income_2021': 'household_income',
            'Poverty_Status': 'poverty_status'
        }

    def test_clean_missing_values(self):
        cleaned_df = clean_missing_values(self.df)
        # Assuming clean_missing_values fills missing numeric with 0 and strings with 'Unknown'
        self.assertEqual(cleaned_df.loc[1, 'Income_2021'], 0)
        self.assertEqual(cleaned_df.loc[3, 'Poverty_Status'], 'Unknown')

    def test_rename_variables(self):
        renamed_df = rename_variables(self.df, self.schema_map)
        # Columns should be renamed
        self.assertIn('household_income', renamed_df.columns)
        self.assertIn('poverty_status', renamed_df.columns)
        self.assertNotIn('Income_2021', renamed_df.columns)

    def test_normalize_column(self):
        # Normalize Income_2021 to 0-1 range
        normalized_df = normalize_column(self.df, 'Income_2021')
        col = normalized_df['Income_2021']
        # Values should be between 0 and 1 (ignoring NaNs)
        self.assertTrue(col.dropna().between(0,1).all())

if __name__ == '__main__':
    unittest.main()
