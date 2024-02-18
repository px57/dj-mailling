# Generated by Django 4.2 on 2024-02-18 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailling', '0005_rename_mail_mailtemplate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailtemplate',
            name='interface',
            field=models.CharField(blank=True, choices=[('DEFAULT', 'DEFAULT'), ('WELCOME', 'WELCOME')], max_length=255, null=True, unique=True),
        ),
    ]