from django.contrib import admin

from .models import Department, Account


class DepartmentAdmin(admin.ModelAdmin):
    model = Department


class AccountAdmin(admin.ModelAdmin):
    model = Account


admin.site.register(Department, DepartmentAdmin)
admin.site.register(Account, AccountAdmin)