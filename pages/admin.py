from django.contrib import admin

# Register your models here.
from pages.models import Barbers, Opening, Appointment, Services, Feedback

admin.site.register(Barbers)
admin.site.register(Opening)
admin.site.register(Appointment)
admin.site.register(Services)
admin.site.register(Feedback)
