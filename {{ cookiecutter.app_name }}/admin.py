from django.contrib import admin

from {{ cookiecutter.app_name }}.models import {{ cookiecutter.model_name }}

# Register your models here.

@admin.register({{ cookiecutter.model_name }})
class {{ cookiecutter.model_name }}Admin(admin.ModelAdmin):
    list_display = ("__str__", )
