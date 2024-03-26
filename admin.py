from django.contrib import admin
from mailling import models

class MailTemplateTranslateInline(admin.TabularInline):
    model = models.MailTemplateTranslation
    extra = 0

    fields = [
        'language',
        'subject', 
        'email_text', 
        'html_src'
    ]
    readonly_fields = ['link']
    formfield_overrides = {}     

    def link(self, obj):
        if obj.pk is None:
            return ''
        return 'test'

@admin.register(models.MailTemplate)
class MailTemplateAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'subject', 
        'interface', 
        'email_text',
    )
    inlines = [MailTemplateTranslateInline]

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
