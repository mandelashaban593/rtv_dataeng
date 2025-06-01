# Data Model Documentation

## Table of Contents
1. [Overview](#overview)  
2. [Models Summary](#models-summary)  
3. [Household Model](#household-model)  
    - [Description](#description)  
    - [Fields](#fields)  
    - [Example Usage](#example-usage)  
4. [Survey Model](#survey-model)  
    - [Description](#description-1)  
    - [Fields](#fields-1)  
    - [Example Usage](#example-usage-1)  
5. [Relationships](#relationships)  
6. [Indexes & Constraints](#indexes--constraints)  
7. [Usage Notes](#usage-notes)  
8. [Migration](#migration)  
9. [Summary](#summary)

---

## Overview

This document provides an overview of the data models used in the `rtv_project` Django application. The models primarily represent household survey data and related entities, enabling efficient storage, retrieval, and analysis of poverty metrics.

---

## Models Summary

| Model Name | Description                       | Key Fields                            |
|------------|-----------------------------------|----------------------------------------|
| Household  | Represents a surveyed household   | `id`, `region`, `household_size`, `income` |
| Survey     | Contains metadata about surveys   | `id`, `survey_date`, `region`, `surveyor_name` |

---

## Household Model

### Description

The `Household` model captures detailed demographic and economic information about a surveyed household.

### Fields

| Field Name        | Data Type      | Description                                 |
|-------------------|----------------|---------------------------------------------|
| `id`              | AutoField (PK) | Unique identifier for each household        |
| `region`          | CharField      | Geographical area or administrative region  |
| `household_size`  | IntegerField   | Number of members in the household          |
| `income`          | DecimalField   | Total monthly or annual household income    |
| `education_level` | CharField      | Highest education level attained in household |
| `access_to_water` | BooleanField   | Indicator if household has access to clean water |
| `has_electricity` | BooleanField   | Indicator if household has electricity access |

### Example Usage

```python
household = Household.objects.create(
    region="Central Uganda",
    household_size=5,
    income=1500000.00,
    education_level="Secondary",
    access_to_water=True,
    has_electricity=False
)
```
## Survey Model
## Description
The Survey model records metadata about each data collection event or survey wave.

## Fields
Field Name	Data Type	Description
id	AutoField (PK)	Unique identifier for each survey
survey_date	DateField	Date when the survey was conducted
region	CharField	Targeted region for the survey
surveyor_name	CharField	Name of the person or team conducting survey
households	ManyToManyField	Link to surveyed Household entries

## Example Usage
```python
survey = Survey.objects.create(
    survey_date="2025-05-15",
    region="Western Uganda",
    surveyor_name="John Doe"
)

survey.households.add(household1, household2)
```
## Relationships
Household to Survey: Many-to-many relationship.

A single survey can include multiple households, and a household may appear in several surveys over time.

## Indexes & Constraints
Index: Applied on region fields for faster geographic queries.

Constraints:

Income must be non-negative

Unique constraint on (survey_date, region) to avoid duplicates

## Usage Notes
The models are extensible. You can add fields like:

Asset ownership

Health indicators

Employment status

Data validation can be strengthened using Django validators or forms.

Migration
After modifying or creating models, run:

python manage.py makemigrations
python manage.py migrate

## Summary
The Household and Survey models are the foundation of the poverty data analysis system. They support efficient data querying, analysis, and integration with dashboards and reports.

## End of Dashboard Guide
Crafted with 💡 by Mandela Shaban

Email: mandelashaban593@gmail.com

Phone: +256763281654

Twitter: mandelashaban51

Instagram:edoctorug1