from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from LINE_bot_app.models import *

class User_Info_Admin(admin.ModelAdmin):
    list_display = ('uid','name','pic_url','mtext','mdt','password')
admin.site.register(User_Info,User_Info_Admin)

class huteAdmin(admin.ModelAdmin):
    list_display=('num','humidity','temperature','mdt')
admin.site.register(hute,huteAdmin)








