from django.contrib import admin
from accounts.models import MyProfile,ActivationCode


admin.site.register(MyProfile)
admin.site.register(ActivationCode)