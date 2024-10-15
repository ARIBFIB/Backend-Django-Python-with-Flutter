# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('api/save/', views.save_data, name='save_data'),  # For API requests
    path('input/', views.input_form, name='input_form'),    # For rendering the HTML form
]
