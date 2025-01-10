from django.contrib import admin
from .models import Username

"""
#define UsernameAdminModel
from .forms import UsernameForm

class UsernameAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_active', 'is_staff')
    list_filter = ('is_active', 'is_staff')
    search_fields = ('username', 'email')
    ordering = ('username',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(is_staff=True)


# Register your models here.
admin.site.register(Username)
"""