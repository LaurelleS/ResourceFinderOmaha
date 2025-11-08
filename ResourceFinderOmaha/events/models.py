
from django.conf import settings
from django.db import models



class TimeStamped(models.Model):
    #this gives other tables 2 columns, and helps us know when things were added
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class Organization(TimeStamped):
    #infomation from the organization hosting an event
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField(blank=True)
    website = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=30, blank=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    #creates tags for people to sort through such as 'Food Pantry', or 'Sports'
    name = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta: #sorts alphabetically
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Location(TimeStamped):
    #where an event happens
    name = models.CharField(max_length=120, blank=True)
    address1 = models.CharField(max_length=200, blank=True)
    address2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=80, default="Omaha")
    state = models.CharField(max_length=2, default="NE")
    postal_code = models.CharField(max_length=15, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name or f"{self.address1}, {self.city}"


class Event(TimeStamped):
    #this is the event itself
    org = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name="events")
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_at = models.DateTimeField()
    end_at = models.DateTimeField(null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.PROTECT, related_name="events")
    is_free = models.BooleanField(default=True)
    url = models.URLField(blank=True)
    capacity = models.PositiveIntegerField(null=True, blank=True)
    categories = models.ManyToManyField(Category, related_name="events", blank=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        indexes = [
            models.Index(fields=["start_at"]),
            models.Index(fields=["is_published"]),
        ]
        ordering = ["start_at"]

    def __str__(self) -> str:
        return self.title


class Subscription(TimeStamped):
    #this is for when a user follows an organization
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="subscriptions")
    org = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name="subscribers")

    class Meta:
        unique_together = ("user", "org")


class Registration(TimeStamped):
    #when the user wants to sign up for the event
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="registrations")
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="registrations")
    status = models.CharField(
        max_length=20,
        choices=[("registered", "Registered"), ("waitlist", "Waitlist"), ("cancelled", "Cancelled")],
        default="registered",
    )

    class Meta:
        unique_together = ("user", "event")