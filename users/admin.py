from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import UserModel


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = UserModel
        fields = ('email',)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")

        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = UserModel
        fields = ('email', 'username', 'password', 'is_active', 'is_admin')


class UserModelAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'is_admin',)
    list_filter = ('is_admin',)
    readonly_fields = ('is_staff', )
    fieldsets = (
        ('Credentials', {'fields': ('email', 'username', 'password')}),
        ('Permissions', {'fields': ('is_admin', 'is_active', 'is_staff',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(UserModel, UserModelAdmin)

# if we are not using Django`s built in permissions
admin.site.unregister(Group)