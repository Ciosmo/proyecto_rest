from django.contrib import admin
from profiles_api import models


admin.site.register(models.userProfile)
admin.site.register(models.ProfileFeedItem)
# Register your models here.
