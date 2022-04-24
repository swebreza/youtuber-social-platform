from django.contrib import admin
from .models import HireTuber
# Register your models here.

# class Hire_Tuber(admin.ModelAdmin):
#  list_display=('id','first_name','last_name','email',)
admin.site.register(HireTuber)
