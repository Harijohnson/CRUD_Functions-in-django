from django.contrib import admin
from userForm.models import user


# Register your models here.
class useradmin(admin.ModelAdmin):
    list_user=['username','email','password']

admin.site.register(user,useradmin)