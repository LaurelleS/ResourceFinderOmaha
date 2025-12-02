from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    location = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Start typing location name...'
        })
    )

    class Meta:
        model = Event
        exclude = ['is_published', 'org', 'created_at', 'updated_at', 'location'] 

        widgets = {
            'start_at': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'form-control'
            }),
            'end_at': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'form-control'
            }),
        }