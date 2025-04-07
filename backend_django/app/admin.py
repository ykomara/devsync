from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Project, Task
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("email", "full_name", "role")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Les mots de passe ne correspondent pas.")
        if len(password2) < 8:
            raise forms.ValidationError("Le mot de passe doit contenir au moins 8 caractères.")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ("email", "full_name", "role", "password", "is_active", "is_staff", "is_superuser", "groups", "user_permissions")

class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    list_display = ('email', 'full_name', 'role', 'is_active', 'is_staff')
    search_fields = ('email', 'full_name')
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informations personnelles', {'fields': ('full_name', 'role')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'full_name', 'role', 'password1', 'password2', 'is_active', 'is_staff')}
        ),
    )



class TaskInline(admin.TabularInline):
    model = Task
    extra = 1  # Nombre de tâches vierges à afficher
    show_change_link = True


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'created_at', 'updated_at')
    search_fields = ('name', 'description', 'owner__email')
    list_filter = ('created_at', 'updated_at')
    filter_horizontal = ('members',)
    inlines = [TaskInline]  # Affiche les tâches dans le projet


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'assignee', 'status', 'priority', 'created_at')
    search_fields = ('title', 'description', 'project__name', 'assignee__email')
    list_filter = ('status', 'priority', 'created_at')
    autocomplete_fields = ['project', 'assignee']

    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'project', 'assignee')
        }),
        ('Détails', {
            'fields': ('status', 'priority')
        }),
        ('Dates', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        })
    )
    readonly_fields = ('created_at', 'updated_at')


admin.site.register(User, CustomUserAdmin)

