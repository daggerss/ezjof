from django.contrib import admin

from .models import JOF

class JOFAdmin(admin.ModelAdmin):
    model = JOF

admin.site.register(JOF, JOFAdmin)
