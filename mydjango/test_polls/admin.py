from django.contrib import admin

# Register your models here.
from .models import LoginUser
# from .forms import LoginForm
admin.site.register(LoginUser)
# admin.site.register(LoginForm)