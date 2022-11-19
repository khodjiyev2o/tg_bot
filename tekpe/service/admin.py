from django.contrib import admin
from .models import Employer,User,Company,Applicant,Worker
# Register your models here.

admin.site.register(Employer)
admin.site.register(User)
admin.site.register(Company)
admin.site.register(Applicant)
admin.site.register(Worker)

