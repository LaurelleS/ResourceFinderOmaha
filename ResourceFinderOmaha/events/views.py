from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .models import Event, Category, Registration
from django.db.models import Q
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
            Q(title__icontains=query) |
            Q(org__name__icontains=query)
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
    is_org = request.user.groups.filter(name='Organizations').exists()

    if not is_org:
        regs = Registration.objects.filter(user=user, status='registered')
        events = [r.event for r in regs]
        context = {
            "events" : events,
            "is_org" : is_org,
            'registrations' : regs
        }
    else:
        my_events = list(Event.objects.filter(org=user.organization))
        context = {
            'events' : my_events,
            'is_org' : is_org,
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

            if not request.user.is_authenticated:
                messages.error(request, 'You must be logged in to register.')
                return redirect('login')
            
            else:
                already_registered = Registration.objects.filter(
                user=request.user,
                event=event).exists() 
                if already_registered:
                    messages.info(request, 'You are already registered for this event')
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
    if already_registered and not messages.get_messages(request):
                messages.info(request, 'You are already registered for this event')
                
    is_org = request.user.groups.filter(name='Organizations').exists()
    context = {
        "event" : event,
        "already_registered" : already_registered,
        'is_org' : is_org
    }
        
    return render(request, "event_detail.html", context)

def addEvent(request):
    if request.method == 'GET':
        form = EventForm()
        return render(request, 'viewEvent.html', {'form' : form})
    else:
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

        return redirect('myevents')
    
def delete_reg(request, reg_id):
    reg = get_object_or_404(Registration, id=reg_id)
    if request.method == 'POST':
        reg.delete()
        messages.success(request, "Registration Deleted.")
        return redirect('myevents')
    
    is_org = request.user.groups.filter(name='Organizations').exists()
    my_events = list(Event.objects.filter(org=request.user.organization))
    context = {
        'events' : my_events,
        'is_org' : is_org,
        'registrations': reg
    }

    return render(request, 'myevents.html', context)

    