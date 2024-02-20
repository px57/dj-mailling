from django.db import models
from kernel.models.base_metadata_model import BaseMetadataModel
from mailling.rules.stack import MAILLING_RULESTACK
from django.forms.models import model_to_dict
from kernel.models.serialize import serializer__serialize__, serializer__init__

class MailTemplateTranslation(BaseMetadataModel):
    """
    MailTemplateTranslation model to store the mail to be sended
    """
    language = models.CharField(
        'language',
        max_length=255,
        default='fr',
        choices=(
            ('fr', 'fr'),
        ),
    )
    
    subject = models.CharField(
        max_length=255, 
        null=True, 
        blank=True,
    )

    email_text = models.TextField(
        null=True, 
        blank=True
    )

    html_src = models.FileField(
        upload_to='mails/',
        null=True,
        blank=True
    )

    translateObject = models.ForeignKey(
        'mailling.MailTemplate',
        on_delete=models.CASCADE,
        related_name='translates',
        blank=True,
        null=True,
    )


    def serialize(self):
        """
        Serialize the model
        """
        serialize = model_to_dict(self)
        return serialize


class MailTemplate(BaseMetadataModel):
    """
    Mail model to store the mail to be sended
    """
    translation_model = MailTemplateTranslation

    @serializer__init__
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    interface = models.CharField(
        max_length=255, 
        null=True, 
        blank=True,
        choices=MAILLING_RULESTACK.models_choices(),
        unique=True,
    )

    subject = models.CharField(
        max_length=255, 
        null=True, 
        blank=True,
    )

    email_text = models.TextField(
        null=True, 
        blank=True
    )

    html_src = models.FileField(
        upload_to='mails/',
        null=True,
        blank=True
    )

    @serializer__serialize__
    def serialize(self, request):
        """
        Serialize the model
        """
        serialize = model_to_dict(self)
        return serialize

class MailSended(BaseMetadataModel):
    """
    MailSended model to store the mail sended by the system
    """
    to = models.JSONField(
        null=True,
        blank=True,
    )

    template = models.ForeignKey(
        'mailling.MailTemplate',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    params = models.JSONField(
        null=True,
        blank=True,
        default=dict
    )

    error = models.JSONField(
        null=True,
        blank=True,
        default=dict
    )


class Unsuscribe(BaseMetadataModel):
    """
    Unsuscribe model to store the unsuscribe request
    """
    profile = models.ForeignKey('profiles.Profile',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    email = models.EmailField(
        null=True,
        blank=True,
    )

    template = models.ForeignKey(   
        'mailling.MailTemplate',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )