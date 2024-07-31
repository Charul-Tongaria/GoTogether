from django.contrib import admin
from .models import CustomUser, Ride  # Your custom user model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'first_name', 'last_name']

class RideAdmin(admin.ModelAdmin):
    list_display = ('driver', 'leaving_from', 'going_to', 'date_of_departure', 'num_passengers')
    list_filter = ('date_of_departure', 'driver')
    search_fields = ('leaving_from', 'going_to', 'driver__username')
    ordering = ('-date_of_departure',)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Ride, RideAdmin)