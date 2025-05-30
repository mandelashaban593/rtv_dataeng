Data Model Documentation
Overview
This document provides an overview of the data models used in the rtv_project Django application. The models primarily represent household survey data and related entities, enabling efficient storage, retrieval, and analysis of poverty metrics.

Models Summary
Model Name	Description	Key Fields
Household	Represents a surveyed household unit	id, region, household_size, income
Survey	Contains metadata about each survey instance	id, survey_date, region, surveyor_name

Household Model
Description
The Household model captures detailed demographic and economic information about a surveyed household.

Fields
Field Name	Data Type	Description
id	AutoField (PK)	Unique identifier for each household
region	CharField	Geographical area or administrative region
household_size	IntegerField	Number of members in the household
income	DecimalField	Total monthly or annual household income
education_level	CharField	Highest education level attained in household
access_to_water	BooleanField	Indicator if household has access to clean water
has_electricity	BooleanField	Indicator if household has electricity access

Example Usage

household = Household.objects.create(
    region="Central Uganda",
    household_size=5,
    income=1500000.00,
    education_level="Secondary",
    access_to_water=True,
    has_electricity=False
)
Survey Model
Description
The Survey model records metadata about each data collection event or survey wave.

Field Name	Data Type	Description
id	AutoField (PK)	Unique identifier for each survey
survey_date	DateField	Date when the survey was conducted
region	CharField	Targeted region for the survey
surveyor_name	CharField	Name of the person or team conducting survey
households	ManyToManyField	Link to surveyed Household entries

Example Usage

survey = Survey.objects.create(
    survey_date="2025-05-15",
    region="Western Uganda",
    surveyor_name="John Doe"
)
survey.households.add(household1, household2)
Relationships
Household to Survey: Many-to-many relationship. One survey can cover many households, and a household could be part of multiple surveys over time.

Indexes & Constraints
Index on region fields for faster geographic queries.

Constraints to ensure income is non-negative.

Unique constraints on survey date and region combination to avoid duplicate surveys.

Usage Notes
The models are designed to be extensible; additional fields such as assets owned, health indicators, or employment status can be added as needed.

Data validation can be enhanced via Django model validators or forms.

Migration
After updating or creating models, run:


python manage.py makemigrations
python manage.py migrate
Summary
The Household and Survey models form the core of the poverty data analysis system, enabling efficient querying and integration with dashboards and reports.