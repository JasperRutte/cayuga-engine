import uuid
from _types import Currency

class Armor:
    def __int__(self, name: str, armor: int, durability: int, required_level: int, currency: Currency):
        self.id = uuid.uuid4()
        self.name = name
        self.armor = armor
        self.durability = durability
        self.required_level = required_level
        self.quality = self.quality_gen()
        self.currency = currency

