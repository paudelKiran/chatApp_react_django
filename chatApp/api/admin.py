from django.contrib import admin
from api.models import Profile,User
# Register your models here.

class profileAdmin(admin.ModelAdmin):
    list_editable = ['verified']
    list_display = ["user","full_name",'verified']


class userAdmin(admin.ModelAdmin):
    list_display = ["id","email"]
   

admin.site.register(Profile,profileAdmin)
admin.site.register(User,userAdmin)