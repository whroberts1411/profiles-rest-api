
from django.contrib import admin
from .models import UserProfile, ProfileFeedItem

#------------------------------------------------------------------------------
class UserProfileAdmin(admin.ModelAdmin):

    list_display = ('email', 'name')

#------------------------------------------------------------------------------
class ProfileFeedItemAdmin(admin.ModelAdmin):

    list_display = ("status_text", "created_on")

#------------------------------------------------------------------------------

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(ProfileFeedItem, ProfileFeedItemAdmin)

#------------------------------------------------------------------------------