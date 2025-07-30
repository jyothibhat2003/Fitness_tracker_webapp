from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Exercise(models.Model):
    name = models.CharField(max_length=100)
    gif = models.ImageField(upload_to='gifs/')

    def __str__(self):
        return self.name

class BodyWeight(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)  # Updated when entry is saved
    weight_kg = models.FloatField()
    body_fat_percent = models.FloatField(null=True, blank=True)  # Optional

    def __str__(self):
        return f"{self.user.username} - {self.weight_kg}kg on {self.date}"

class BodyMeasurement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()

    # Arms
    left_arm_cm = models.FloatField()
    right_arm_cm = models.FloatField()

    # Forearms
    left_forearm_cm = models.FloatField()
    right_forearm_cm = models.FloatField()

    # Chest
    chest_cm = models.FloatField()

    # Abdomen
    abdomen_cm = models.FloatField()

    # Shoulders
    shoulders_cm = models.FloatField()

    # Hips (Cadera)
    hips_cm = models.FloatField()

    # Legs
    left_leg_cm = models.FloatField()
    right_leg_cm = models.FloatField()

    # Calves
    left_calf_cm = models.FloatField()
    right_calf_cm = models.FloatField()

    # Glutes (Trasero)
    glutes_cm = models.FloatField()

    def __str__(self):
        return f"{self.user.username} - {self.date}"


class WorkoutSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.date}"

class SetEntry(models.Model):
    session = models.ForeignKey(WorkoutSession, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    reps = models.PositiveIntegerField()
    weight_kg = models.FloatField()
    rpe = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 11)])
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.exercise.name} - {self.reps} reps - {self.weight_kg}kg"