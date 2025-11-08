
from django.contrib import admin
from .models import Organization, Category, Location, Event, Subscription, Registration

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("name", "is_verified", "website", "email", "created_at")
    search_fields = ("name", "email")
    readonly_fields = ("created_at", "updated_at")

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name", "slug")

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("name", "city", "state", "postal_code", "created_at")
    search_fields = ("name", "address1", "city")
    readonly_fields = ("created_at", "updated_at")

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "org", "start_at", "is_free", "is_published")
    list_filter = ("is_published", "is_free", "categories")
    search_fields = ("title", "description")
    autocomplete_fields = ("org", "location", "categories")
    date_hierarchy = "start_at"
    list_select_related = ("org", "location")
    ordering = ("start_at",)
    list_per_page = 25
    readonly_fields = ("created_at", "updated_at")  

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ("user", "org", "created_at")
    search_fields = ("user__username", "org__name")
    readonly_fields = ("created_at", "updated_at")

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ("user", "event", "status", "created_at")
    list_filter = ("status",)
    search_fields = ("user__username", "event__title")
    readonly_fields = ("created_at", "updated_at")