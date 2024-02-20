

from django.conf import settings
from mailling.rules.stack import MAILLING_RULESTACK
from kernel.interfaces.interfaces import InterfaceManager


class DefaultRuleClass(InterfaceManager):
    """
    The default rule class. 
    """

    """
    Is the service mail to be used.
    """
    service_mail = settings.MAILLING_SERVICE

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

    def gpm_pre_init(self):
        """
        The gpmInit method.
        """

    def gpm_init(self):
        """
        The gpmInit method.
        """
        print ('gpmInit###' * 10)
        template_info = self.distant_load_template()
        self.template = self.load_template()
    
    """
    Load the template in the distant services.
    """
    def distant_load_template(self, *args, **kwargs):
        return None
    
    """
    Update the template in the distant services.
    """
    def distant_update_template(self, *args, **kwargs):
        return True
    
    """
    Load database template.
    """
    def load_template(self, *args, **kwargs):
        from mailling.models import MailTemplate
        return MailTemplate.objects.get(interface=self.label)

    """
    Update the template in the database.
    """
    def update_template(self, dbTemplate):
        self.template = dbTemplate
    
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