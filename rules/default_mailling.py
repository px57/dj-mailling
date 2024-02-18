

from mailling.rules.stack import MAILLING_RULESTACK
from kernel.interfaces.interfaces import InterfaceManager

class DefaultRuleClass(InterfaceManager):
    """
    The default rule class. 
    """

    """
    The label to identify the rule interface.
    """
    label = 'DEFAULT'

    """
    The allow flag to enable or disable the rule.
    """
    allow = True

    def __init__(self) -> None:
        super().__init__()

    """
    The constructor method.
    """
    def check(self, *args, **kwargs):
        return True

    """
    The run method.
    """   
    def run(self, *args, **kwargs):
        return True

    """
    The error method.
    """
    def error(self, *args, **kwargs):
        return True
    
    """
    After send the notification, the response method is called.
    """
    def response(self, *args, **kwargs):
        return True
    
    """
    The click method.
    """
    def click(self, *args, **kwargs):
        return True

    """
    The open method.
    """
    def open(self, *args, **kwargs):
        return True

MAILLING_RULESTACK.set_rule(DefaultRuleClass())