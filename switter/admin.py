from django.contrib import admin
from django.contrib.auth import models
from django.contrib.auth.models import Group, User
from django.db.models import fields
# Register your models here.
from . models import Profile

admin.site.register(Profile)
class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ['username']


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
