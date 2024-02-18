from django.db import models
from kernel.models.base_metadata_model import BaseMetadataModel
from mailling.rules.stack import MAILLING_RULESTACK

class Mail(BaseMetadataModel):
    """
    Mail model to store the mail to be sended
    """
    interface = models.CharField(
        max_length=255, 
        null=True, 
        blank=True,
        choices=MAILLING_RULESTACK.models_choices()
    )

    subject = models.CharField(
        max_length=255, 
        null=True, 
        blank=True
    )

    body = models.TextField(
        null=True, 
        blank=True
    )

    html_src = models.FileField(
        upload_to='mails/',
        null=True,
        blank=True
    )

class MailSended(BaseMetadataModel):
    """
    MailSended model to store the mail sended by the system
    """
    to = models.JSONField(
        null=True,
        blank=True
    )

    mail = models.ForeignKey(
        'mailling.Mail',
        on_delete=models.CASCADE,
        null=True,
        blank=True
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

    mail = models.EmailField(
        max_length=255,
        null=True,
        blank=True
    )

    email_key = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )