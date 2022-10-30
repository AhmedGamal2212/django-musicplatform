from django.contrib import admin
from django import forms
from .models import CustomUser


class UserAminForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = '__all__'
        exclude = {
            'password1',
            'password2'
        }
        widgets = {
            'bio': forms.Textarea(),
        }


class UserAdmin(admin.ModelAdmin):
    form = UserAminForm


admin.site.register(CustomUser, UserAdmin)
