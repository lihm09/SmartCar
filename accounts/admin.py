from django.contrib import admin
from accounts.models import MyProfile

class MyProfileAdmin(admin.ModelAdmin):
    #list_display = ("user","student_number","grade","class_name","mobile","address","gender","birthday")
    radio_fields = {'gender':admin.HORIZONTAL}

admin.site.register(MyProfile,MyProfileAdmin)