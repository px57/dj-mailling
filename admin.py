from django.contrib import admin
from mailling import models

@admin.register(models.MailTemplate)
class MailTemplateAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'subject', 
        'interface', 
        'email_text',
    )

@admin.register(models.MailSended)
class MailSendedAdmin(admin.ModelAdmin):
    list_display = (
        # 'id', 
        # 'template', 
        # 'to', 
        # 'status',
    )

@admin.register(models.Unsuscribe)
class UnsuscribeAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
    )
