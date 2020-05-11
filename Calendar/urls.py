from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'cal'
urlpatterns = [
    path('events/', views.CalendarView.as_view(), name='calendar'),
    path('add_event/', views.EventAddView.as_view()),
    path('update_event/<pk>', views.EventUpdateView.as_view()),
]
