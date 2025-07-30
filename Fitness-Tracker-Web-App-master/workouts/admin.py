from django.contrib import admin
from .models import Exercise, BodyWeight, BodyMeasurement, WorkoutSession, SetEntry

# Register your models here.
admin.site.register(Exercise)
admin.site.register(BodyWeight)
admin.site.register(BodyMeasurement)
admin.site.register(WorkoutSession)
admin.site.register(SetEntry)