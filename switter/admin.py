from statistics import mode
from django.contrib import admin
from django.contrib.auth import models
from django.contrib.auth.models import Group, User
from django.db.models.signals import post_save
from django.db.models import fields
# Register your models here.
from . models import Profile, Sweet
class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ['username']
    inlines  = [ProfileInline]

admin.site.register(Sweet)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)

def create_profile(sender,instance,created,**kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        user_profile.follows.set([instance.profile.id])
        user_profile.save()

post_save.connect(create_profile,sender=User)
