from django.contrib import admin
from .models import SignUp, User
from .forms import SignUpForm, UserForm


class SignUpAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'email', 'timestamp', 'updated']
    form = SignUpForm


class UserAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'email', 'password']
    form = UserForm


admin.site.register(SignUp, SignUpAdmin)
admin.site.register(User, UserAdmin)
