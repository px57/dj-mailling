"""
This module contains the views for the mailling app.
"""

from django.shortcuts import render

from gpm.http import Response

from mailling.rules.stack import MAILLING_RULESTACK
from mailling.models import Unsuscribe

from profiles.models import Profile

def unsubscribe(request):
    """
    Unsubscribe the user from the mailling list.

    Args:
        request.GET._in (str): The interface name.
        request.GET.email (str): The email to be unsubscribed.
    """
    res = Response(request=request)
    str_in = request.GET['_in']
    email = request.GET['email']
    
    _in = MAILLING_RULESTACK.get_rule(str_in)
    if _in.unsubscribe_enable == False:
        return res.error('The interface does not allow to unsubscribe.')
    
    dbProfile = Profile.objects.filter(email=email).first()
    dbUnsuscribe = Unsuscribe(
        email=email,
        interface=str_in,
        profile=dbProfile,
    )
    dbUnsuscribe.save()
    res.unsuscribe = dbUnsuscribe.serialize(request)
    return res.success()

def subscribe(request):
    """
    Subscribe the user to the mailling list.

    Args:
        request.GET._in (str): The interface name.
        request.GET.email (str): The email to be subscribed.
    """
    res = Response(request=request)
    str_in = request.GET['_in']
    email = request.GET['email']
    
    _in = MAILLING_RULESTACK.get_rule(str_in)
    if _in.unsubscribe_enable == False:
        return res.error('The interface does not allow to subscribe.')
    
    Unsuscribe.objects.filter(email=email).delete()
    Unsuscribe.objects.filter(profile__email=email).delete()
    return res.success()