from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('task', 'is_completed', 'updated_at')
    search_fields = ('task',)
# Register your models here.
admin.site.register(Task, TaskAdmin)

#this file register 
#list_display is attribute use to show backend data
#search_fields is also attribute