from django.shortcuts import render
from .models import Event, Category


def home(request):
    # Get filters from the query string (?q=...&category=...)
    query = request.GET.get("q", "").strip()
    category_slug = request.GET.get("category", "").strip()

    # Base queryset: only published events, ordered by start time
    events = Event.objects.filter(is_published=True).order_by("start_at")

    if query:
        events = events.filter(
            models.Q(title__icontains=query)
            | models.Q(org__name__icontains=query)
        )

    if category_slug:
        events = events.filter(categories__slug=category_slug)

    # Avoid duplicates when filtering by many-to-many
    events = events.distinct()

    categories = Category.objects.order_by("name")
    is_org = request.user.groups.filter(name='Organizations').exists()

    context = {
        "events": events,
        "categories": categories,
        "query": query,
        "selected_category": category_slug,
        "is_org": is_org
    }
    return render(request, "home.html", context)