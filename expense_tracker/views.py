from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.urls import reverse
from django.conf import settings


def welcome(request):
    """Display a welcome message with the user's name and email."""
    user = request.user
    if user.is_authenticated:
        context = {
            'name': user.get_full_name(),
            'email': user.email,
        }
        return render(request, 'welcome.html', context)
    return redirect('login')



def logout_view(request):
    """Log out the user and redirect to the ADFS logout URL."""
    # Clear the Django session
    logout(request)

    # Get the ADFS logout URL from your settings
    adfs_logout_url = settings.LOGOUT_URL # Make sure to define this in your AUTH_ADFS

    # Redirect to the ADFS logout URL if it is defined
    if adfs_logout_url:
        # Redirect to ADFS logout and return
        return redirect(adfs_logout_url)
    else:
        # If ADFS logout URL is not set, redirect to login page
        return redirect('login')


def custom_404_view(request, exception):
    """Custom view for handling 404 errors."""
    return render(request, '404.html', {}, status=404)