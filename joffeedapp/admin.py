from django.contrib import admin

from .models import JOF, Draft

class JOFAdmin(admin.ModelAdmin):
    model = JOF

class DraftAdmin(admin.ModelAdmin):
    model = Draft

admin.site.register(JOF, JOFAdmin)
admin.site.register(Draft, DraftAdmin)