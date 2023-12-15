from django.contrib import admin
from .models import Candidatedirectory, Eventdetails, Educationlevel, Jobrequisition, Persona, Screeningmode, Gender, Maritalstatus, Employeedirectory, City, Experiencelevel, Reasonforchange
# Register your models here.

admin.site.register(Candidatedirectory)
admin.site.register(Eventdetails)
admin.site.register(Jobrequisition)
admin.site.register(Persona)
admin.site.register(Screeningmode)
admin.site.register(Gender)
admin.site.register(Maritalstatus)
admin.site.register(Employeedirectory)
admin.site.register(City)
admin.site.register(Experiencelevel)
admin.site.register(Educationlevel)
admin.site.register(Reasonforchange)