from django.urls import path, include
from .views import welcome, logout_view

urlpatterns = [
    path('welcome/', welcome, name='welcome'),  # Welcome page URL
    path('', logout_view, name='logout'),  # Logout view
]

