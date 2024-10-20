from django.db import models

class DailyWeatherSummary(models.Model):
    date = models.DateField()
    average_temp = models.FloatField()
    max_temp = models.FloatField()
    min_temp = models.FloatField()
    dominant_condition = models.CharField(max_length=50)

    def __str__(self):
        return f"Weather Summary for {self.date}"
