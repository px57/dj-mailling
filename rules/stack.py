

from gpm.interfaces.stack import RulesStack
from gpm.message.centralize import MESSAGE_SWITCHER

MAILLING_RULESTACK = RulesStack()
MESSAGE_SWITCHER.load_stack(MAILLING_RULESTACK)