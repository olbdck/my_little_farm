from django.contrib import admin
from .models import Farmers

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "cows_in_own", "joined_date",) 
    
admin.site.register(Farmers, MemberAdmin)