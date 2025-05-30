from django.db import models

# -- Geographic Models --

class District(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class SubCounty(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}, {self.district.name}"

class Village(models.Model):
    name = models.CharField(max_length=100)
    sub_county = models.ForeignKey(SubCounty, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}, {self.sub_county.name}"

# -- Household Model --

class Household(models.Model):
    household_id = models.CharField(max_length=50, unique=True)
    head_name = models.CharField(max_length=100, blank=True)
    village = models.ForeignKey(Village, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"HH-{self.household_id} ({self.village})"

# -- Survey Model --

class Survey(models.Model):
    SURVEY_CYCLE_CHOICES = [
        ('baseline', 'Baseline'),
        ('year1', 'Year 1 Follow-up'),
        ('year2', 'Year 2 Follow-up'),
    ]

    household = models.ForeignKey(Household, on_delete=models.CASCADE)
    survey_cycle = models.CharField(max_length=20, choices=SURVEY_CYCLE_CHOICES)
    survey_date = models.DateField()
    total_income = models.FloatField(null=True, blank=True)
    total_expenditure = models.FloatField(null=True, blank=True)
    food_security_score = models.FloatField(null=True, blank=True)
    school_enrollment = models.IntegerField(null=True, blank=True)
    water_access = models.BooleanField(default=False)
    latrine_access = models.BooleanField(default=False)
    remarks = models.TextField(blank=True)

    def __str__(self):
        return f"{self.household.household_id} - {self.survey_cycle}"
