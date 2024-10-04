
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('oauth2/', include('django_auth_adfs.urls')),
    path('', include('expense_tracker.urls')),
]

handler404 = 'expense_tracker.views.custom_404_view'


