from django.db.models import Avg, Count, Q
from core.models import Survey

def average_income():
    result = Survey.objects.aggregate(avg_income=Avg('total_income'))
    return result['avg_income'] or 0

def average_expenditure():
    result = Survey.objects.aggregate(avg_expenditure=Avg('total_expenditure'))
    return result['avg_expenditure'] or 0

def poverty_headcount(threshold=1.9):
    """
    Calculates the proportion of households below the international poverty line (USD 1.90/day).
    Assumes total_income is monthly. Adjust as needed for your dataset.
    """
    count_total = Survey.objects.count()
    if count_total == 0:
        return 0

    below_line = Survey.objects.filter(total_income__lt=threshold * 30).count()
    return round(below_line / count_total, 2)

def food_insecurity_rate(threshold=3):
    """
    Percentage of households with food security score below a critical threshold.
    """
    count_total = Survey.objects.count()
    if count_total == 0:
        return 0

    insecure = Survey.objects.filter(food_security_score__lt=threshold).count()
    return round(insecure / count_total, 2)

def latrine_access_rate():
    """
    Percentage of households with access to latrines.
    """
    count_total = Survey.objects.count()
    if count_total == 0:
        return 0

    with_access = Survey.objects.filter(latrine_access=True).count()
    return round(with_access / count_total, 2)

def water_access_rate():
    """
    Percentage of households with access to safe water.
    """
    count_total = Survey.objects.count()
    if count_total == 0:
        return 0

    with_access = Survey.objects.filter(water_access=True).count()
    return round(with_access / count_total, 2)

def school_enrollment_rate():
    """
    Percentage of households with children enrolled in school.
    """
    count_total = Survey.objects.count()
    if count_total == 0:
        return 0

    enrolled = Survey.objects.filter(school_enrollment=True).count()
    return round(enrolled / count_total, 2)

def all_metrics():
    """
    Returns all KPIs in a dictionary.
    """
    return {
        'Average Income': average_income(),
        'Average Expenditure': average_expenditure(),
        'Poverty Headcount Ratio': poverty_headcount(),
        'Food Insecurity Rate': food_insecurity_rate(),
        'Latrine Access Rate': latrine_access_rate(),
        'Water Access Rate': water_access_rate(),
        'School Enrollment Rate': school_enrollment_rate(),
    }
