from django.contrib import admin
from .models import UserProfile, NewsletterSubscription


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'default_phone_number', 'default_country', 'profile_image')

    # Hide any profiles without a username/null
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.exclude(user__username=None)


@admin.register(NewsletterSubscription)
class NewsletterSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_on')
