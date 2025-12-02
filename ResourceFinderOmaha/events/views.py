from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .models import Event, Category, Registration
from .forms import EventForm
from django.core.exceptions import PermissionDenied


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


def myevents(request):
    user = request.user
    regs = Registration.objects.filter(user=user, status='registered')
    events = [r.event for r in regs]
    is_org = request.user.groups.filter(name='Organizations').exists()
    context = {
         "events" : events,
         "is_org" : is_org
    }
    return render(request, 'myevents.html', context)

def viewEvent(request, event_id):
    event = Event.objects.get(pk=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('myevents')
    else:
        form = EventForm(instance=event)

    return render(request, 'viewEvent.html', {'form' : form})
 

def eventDetail(request, event_id):
    event = Event.objects.get(pk=event_id)

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'register':
            user = request.user

            if not request.user.is_authenticated:
                messages.error(request, 'You must be logged in to register.')
                return redirect('login')
            
            else:
                Registration.objects.create(
                    user=request.user,
                    event=event
                )
                messages.success(request, "You are now registered for this event!")
            return redirect('eventDetail', event_id=event_id)
        
    already_registered = False
    already_registered = Registration.objects.filter(
            user=request.user,
            event=event).exists() 
    
    if already_registered:
                messages.info(request, 'You are already registered for this event')
   
    context = {
        "event" : event,
        "already_registered" : already_registered
    }
        
    return render(request, "event_detail.html", context)

    