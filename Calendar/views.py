from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from datetime import datetime, date
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe
from django.views.generic import UpdateView, CreateView
from .models import *
from .utils import Calendar


class CalendarView(generic.ListView):
    model = Event
    template_name = 'calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('day', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['Calendar'] = mark_safe(html_cal)
        return context


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()


class EventAddView(LoginRequiredMixin, CreateView):
    model = Event
    fields = ['title', 'description', 'start_date', 'end_date']
    template_name = 'add_event.html'
    success_url = '/calendar/events/'


class EventUpdateView(LoginRequiredMixin, UpdateView):
    model = Event

    fields = ['title', 'description', 'start_date', 'end_date']
    template_name = 'edit_event.html'
    success_url = '/calendar/events/'
