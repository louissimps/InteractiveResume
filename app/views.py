"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from app.models import Contact, WorkHistory, Education, WorkSkill
def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)

    work_histories = WorkHistory.objects.all().order_by('-start_date')

    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
            'contact': Contact.objects.get(pk=1),
            'current_position': WorkHistory.objects.get(is_current='True'),
            'work_histories': work_histories,
        })
    )



def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        context_instance = RequestContext(request,
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
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
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
            'contact': Contact.objects.get(pk=1),

        })
    )

def history(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/history.html',
        context_instance = RequestContext(request,
        {
            'title':'Work History',
            'contact': Contact.objects.get(pk=1),
            'work_histories': WorkHistory.objects.all().order_by('-start_date'),

        })
    )
