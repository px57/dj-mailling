

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
    _service = settings.MAILLING_SERVICE

    """

    The label to identify the rule interface.
    """
    label = 'DEFAULT'

    """
    The allow flag to enable or disable the rule.
    """
    allow = True

    """
    Unsuscribe enable flag.
        1. Don't generate the unsubscribe link.
        2. Don't check if the mail has an unsubscribe link.
        3. Don't accept the unsubscribe link.
    """
    unsubscribe_enable = True

    def __init__(self) -> None:
        super().__init__()

    def gpm_init(self, **kwargs):
        """
        The gpmInit method.
        """
        super().gpm_init()
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
        dbMailTemplate = MailTemplate.objects.filter(interface=self.label)
        if not dbMailTemplate.exists():
            dbMailTemplate = self.distant_load_template()
            if dbMailTemplate is None:
                dbMailTemplate = MailTemplate.objects.create(
                    interface=self.label,
                    subject=self.label,
                )
                dbMailTemplate.save()
                return dbMailTemplate
        return dbMailTemplate.first()

    """
    Update the template in the database.
    """
    def update_template(self, dbTemplate):
        self.template = dbTemplate

    def __mail_has_unsubscribe(self, **kwargs):
        """
        Check if the mail has an unsubscribe link.
        """
        from mailling.models import Unsuscribe
        if self.unsubscribe_enable:
            return False
        
        # dbUnsuscribe = Unsuscribe.objects.get(email=kwargs.get('to'))
        return False

    def __generate_unsubscribe_link(
            self, 
            res=None,
            sendTo=None,
        ):
        """
        Generate the unsubscribe link.
        """
        return res.create_client_url(f'/v1/mailling/unsubscribe/?email={sendTo.email}&_in={self.label}')

    def __get_ctx(
            self, 
            res=None, 
            sendTo=None, 
            params=None
        ):
        """
        Get the context.

        Args:
            res: The response object.
            sendTo: Send to profile 
            params: The params object.
        """
        ctx = {
            'UNSUBSCRIBE_LINK': self.__generate_unsubscribe_link(
                res=res, 
                sendTo=sendTo
            ),
        }
        ctx.update(params)
        return ctx
    
    def send(
        self, 
        _inSwitch=None,
        res=None,
        sendTo=None,
        sendBy=None,
        params=None, 
        ):
        """
        Send the mail.

        Args:
            _inSwitch: The switcher object.
            res: The response object.
            sendTo: Send to profile 
            sendBy: Send by profile 
            params: The params object.
        """
        if not self.allow:
            return False

        if not self._service:   
            return False

        print ('SEND MAIL 1')    
        if self.__mail_has_unsubscribe(sendTo=sendTo):
            return False

        print ('SEND MAIL 2')
        dbTemplate = self.load_template()
        ctx = self.__get_ctx(
            res=res,
            sendTo=sendTo,
            params=params
        )

        return True

MAILLING_RULESTACK.set_rule(DefaultRuleClass)
