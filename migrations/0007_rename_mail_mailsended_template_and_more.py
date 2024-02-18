# Generated by Django 4.2 on 2024-02-18 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mailling', '0006_alter_mailtemplate_interface'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mailsended',
            old_name='mail',
            new_name='template',
        ),
        migrations.RenameField(
            model_name='mailtemplate',
            old_name='body',
            new_name='email_text',
        ),
        migrations.RemoveField(
            model_name='unsuscribe',
            name='email_key',
        ),
        migrations.RemoveField(
            model_name='unsuscribe',
            name='mail',
        ),
        migrations.AddField(
            model_name='unsuscribe',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='unsuscribe',
            name='template',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mailling.mailtemplate'),
        ),
    ]