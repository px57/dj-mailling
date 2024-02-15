from django.db import models
from kernel.models.base_metadata_model import BaseMetadataModel

class MailSended(BaseMetadataModel):
    """
    MailSended model to store the mail sended by the system
    """
    mail = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    subject = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    body = models.TextField(null=True,
        blank=True
    )
    status = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    error = models.TextField(null=True,
        blank=True
    )
    error_trace = models.TextField(null=True,
        blank=True
    )
    response = models.TextField(null=True,
        blank=True
    )
    response_trace = models.TextField(null=True,
        blank=True
    )
    response_code = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    response_message = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    response_status = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    response_error = models.TextField(null=True,
        blank=True
    )
    response_error_trace = models.TextField(null=True,
        blank=True
    )
    response_error_code = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    response_error_message = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    response_error_status = models.CharField(
        max_length=255,
        null=True,
        blank=True
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