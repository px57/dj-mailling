

from kernel.interfaces.stack import RulesStack
from kernel.message.centralize import MESSAGE_SWITCHER

MAILLING_RULESTACK = RulesStack()
MESSAGE_SWITCHER.load_stack(MAILLING_RULESTACK)