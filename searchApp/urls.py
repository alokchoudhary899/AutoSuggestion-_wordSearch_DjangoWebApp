from django.urls import path
from searchApp import views
app_name = 'searchApp'
urlpatterns = [
 path('search/', views.IndexView.as_view(), name='search'),
 path('Wsearch/', views.wordAutocomplete, name='Wsearch'),
]