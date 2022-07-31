from django.urls import path
from . import views

# register the app namespace
# URL NAMES
app_name = 'book'

urlpatterns = [
    path('', views.cover_view, name='cover'),
    path('var/', views.variable_view, name='var'),
]