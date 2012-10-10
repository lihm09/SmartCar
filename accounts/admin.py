from django.contrib import admin
from accounts.models import MyProfile,ActivationCode

class MyProfileAdmin(admin.ModelAdmin):
    #list_display = ("user","student_number","grade","class_name","mobile","address","gender","birthday")
    radio_fields = {'gender':admin.HORIZONTAL}

admin.site.register(MyProfile,MyProfileAdmin)
admin.site.register(ActivationCode)