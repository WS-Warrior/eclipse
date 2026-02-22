from django.contrib import admin
from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'is_staff', 'user_lvl', 'user_rank']
    search_fields = ['id', 'username', 'email', 'user_rank']