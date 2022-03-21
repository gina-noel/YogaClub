from django.contrib import admin
from .models import Classes, ClassDetail, Pricing, Schedule
# Register your models here.
admin.site.register(Classes)
admin.site.register(ClassDetail)
admin.site.register(Pricing)
admin.site.register(Schedule)