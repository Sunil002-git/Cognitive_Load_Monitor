from django.db import models

class FatigueLog(models.Model):
    blink_rate = models.FloatField()
    fatigue_score = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Fatigue: {self.fatigue_score}"