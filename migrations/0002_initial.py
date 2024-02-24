# Generated by Django 4.2 on 2024-02-24 00:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
        ('mailling', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='unsuscribe',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.profile'),
        ),
        migrations.AddField(
            model_name='unsuscribe',
            name='template',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mailling.mailtemplate'),
        ),
        migrations.AddField(
            model_name='mailtemplatetranslation',
            name='translateObject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translates', to='mailling.mailtemplate'),
        ),
        migrations.AddField(
            model_name='mailsended',
            name='template',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mailling.mailtemplate'),
        ),
    ]
