from typing import NewType
from typing import Union

Stat = Union[NewType("strength", str), NewType("wisdom", str), NewType("intelligence", str), NewType("dexterity", str), NewType("charisma", str), NewType("constitution", str)]
Currency =  NewType("currency", int)
