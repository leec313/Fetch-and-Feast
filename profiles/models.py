import uuid
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
    """
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    default_email = models.EmailField(max_length=254, null=False, blank=False)
    default_phone_number = models.CharField(
        max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(
        max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(
        max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(
        max_length=40, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(
        blank_label='Country', null=True, blank=True)
    profile_image = models.ImageField(
        null=True, blank=True, upload_to='profile-images')
    subscribe_newsletter = models.BooleanField(default=False)

    def __str__(self):
        if self.user:
            return self.user.username
        else:
            return "No associated user"


class NewsletterSubscription(models.Model):
    """
    Defines Newsletter subscription model
    """
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    created_on = models.DateTimeField(auto_now_add=True)

    # Use a callable instead of a static method for the default value
    def default_token():
        return uuid.uuid4()

    unsubscribe_token = models.UUIDField(default=default_token, editable=False)

    def __str__(self):
        return self.email  # Return email for string representation


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        profile = UserProfile.objects.create(user=instance)
    else:
        profile = instance.userprofile

    # Check if 'profile_image' is not set
    if not profile.profile_image:
        profile.profile_image = 'default-images/default_profile.webp'

    # Save the profile
    profile.save()


@receiver(pre_delete, sender=NewsletterSubscription)
def update_user_profile_on_newsletter_delete(sender, instance, **kwargs):
    """
    Update user profile subscribe_newsletter
    field when a newsletter subscription is deleted
    """
    user_profile = instance.user_profile
    user_profile.subscribe_newsletter = False
    user_profile.save()
