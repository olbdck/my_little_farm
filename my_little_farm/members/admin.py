from django.contrib import admin
from .models import Farmer, Cow

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "cows_in_own", "joined_date",) 
    
admin.site.register(Farmer, MemberAdmin)
admin.site.register(Cow)