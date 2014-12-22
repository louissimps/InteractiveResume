"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from app.models import *
import itertools
from django.utils.text import slugify


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    wh = WorkHistory.objects.get(is_current='True')
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title': 'Home Page',
            'year': datetime.now().year,
            'contact': Contact.objects.get(pk=1),
            'current_position': wh,
            'current_resume': Resume.objects.get(is_default=True),
            'current_application': Application.objects.get(pk=1),
            'current_skills': WorkSkill.objects.filter(work_history=wh).select_related().order_by('-skill_proficiency_level'),
        })
    )



def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        context_instance=RequestContext(request,
        {
            'title': 'Contact',
            'message': 'Your contact page.',
            'year': datetime.now().year,
        })
    )


def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        context_instance = RequestContext(request,
        {
            'title': 'About',
            'message': 'Your application description page.',
            'year': datetime.now().year,
            'contact': Contact.objects.get(pk=1),

        })
    )


def history(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/history.html',
        context_instance=RequestContext(request,
        {
            'title': 'Work History',
            'contact': Contact.objects.get(pk=1),
            'work_histories': WorkHistory.objects.all().order_by('-start_date'),
            'current_application': Application.objects.get(pk=1),

        })
    )

def education(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/education.html',
        context_instance=RequestContext(request,
        {
            'current_application': Application.objects.get(pk=1),
            'education': Education.objects.all().order_by('school_name'),

        })
    )


def workhistory(request, id, slug):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    wh = WorkHistory.objects.get(pk=id)
    return render(
        request,
        'app/workhistory.html',
        context_instance = RequestContext(request,
        {
            'title': 'Work History Detail',
            'work_history': wh,
            'current_application': Application.objects.get(pk=1),
            'current_skills': WorkSkill.objects.filter(work_history=wh).select_related().order_by('-skill_proficiency_level'),
        })
    )
