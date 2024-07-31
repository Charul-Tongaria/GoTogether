from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout, login, update_session_auth_hash
from .models import Ride, CustomUser
from .forms import RideForm, CustomUserChangeForm, CustomUserCreationForm, CustomAuthenticationForm, CustomPasswordChangeForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError  # Import IntegrityError

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
def create_ride(request):
    if request.method == 'POST':
        form = RideForm(request.POST)
        if form.is_valid():
            try:
                ride = form.save(commit=False)
                ride.driver = request.user  # Assign the current user as the driver
                ride.save()
                messages.success(request, 'Ride created successfully!')
                return redirect('ride_list')  # Redirect to the ride list page
            except IntegrityError as e:
                messages.error(request, 'An error occurred while saving the ride. Please try again.')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = RideForm()

    return render(request, 'create_ride.html', {'form': form})

# def ride_list(request):
#     if request.method == 'GET':
#         leaving_from = request.GET.get('leaving_from')
#         going_to = request.GET.get('going_to')
#         date_of_departure = request.GET.get('date_of_departure')
#         Rides = Ride.objects.filter(
#             leaving_from=leaving_from,
#             going_to=going_to,
#             date_of_departure=date_of_departure
#         )
#     return render(request, 'ride_list.html', {'Rides': Rides})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def scam_info(request):
    return render(request, 'scam_info.html')

def carpool_bonus_info(request):
    # Your carpool_bonus_info view logic
    return render(request, 'carpool_bonus_info.html')

def profile_view(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    return render(request, 'profile.html', {'user': user})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        password_form = CustomPasswordChangeForm(user=request.user, data=request.POST)

        if form.is_valid() and password_form.is_valid():
            # Save the user info
            form.save()

            # Handle password change
            if password_form.cleaned_data.get('new_password1'):
                if password_form.cleaned_data['new_password1'] != password_form.cleaned_data['old_password']:
                    request.user.set_password(password_form.cleaned_data['new_password1'])
                    request.user.save()
                    update_session_auth_hash(request, request.user)  # Keep user logged in after password change
                    messages.success(request, 'Your profile was successfully updated and password changed!')
                else:
                    password_form.add_error('new_password1', 'New password cannot be the same as the old password.')
                    messages.error(request, 'New password cannot be the same as the old password.')
                    return render(request, 'edit_profile.html', {'form': form, 'password_form': password_form})

            messages.success(request, 'Your profile was successfully updated!')
            return redirect('profile')

        else:
            messages.error(request, 'Please correct the errors below.')
            return render(request, 'edit_profile.html', {'form': form, 'password_form': password_form})

    else:
        form = CustomUserChangeForm(instance=request.user)
        password_form = CustomPasswordChangeForm(user=request.user)
    
    return render(request, 'edit_profile.html', {'form': form, 'password_form': password_form})

@login_required
def ride_list(request):
    leaving_from = request.GET.get('leaving_from')
    going_to = request.GET.get('going_to')
    date_of_departure = request.GET.get('date_of_departure')
    num_passengers = request.GET.get('passenger_count', 1)  # Default to 1 if not provided

    # Filter rides based on search parameters
    rides = Ride.objects.all()
    if leaving_from:
        rides = rides.filter(leaving_from__icontains=leaving_from)
    if going_to:
        rides = rides.filter(going_to__icontains=going_to)
    if date_of_departure:
        rides = rides.filter(date_of_departure=date_of_departure)
    if num_passengers:
        rides = rides.filter(num_passengers__gte=int(num_passengers))
    context = {
        'rides': Ride.objects.all(),
    }
    return render(request, 'ride_list.html', {'rides': rides})

@login_required
def delete_ride(request, ride_id):
    ride = get_object_or_404(Ride, id=ride_id)

    # Check if the user is the creator of the ride
    if ride.driver == request.user:
        ride.delete()
        messages.success(request, 'Ride deleted successfully!')
    else:
        messages.error(request, 'You do not have permission to delete this ride.')

    return redirect('ride_list')