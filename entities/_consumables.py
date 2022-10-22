import uuid
from _types import Currency


class Consumable:
    def __init__(self, name: str, health_regen: int, health_over_time: int, stamina_regen: int, stamina_over_time: int, currency: Currency):
        self.id = uuid.uuid4()
        self.name = name
        self.health_regen = health_regen
        self.health_over_time = health_over_time
        self.stamina_regen = stamina_regen
        self.stamina_over_time = stamina_over_time
        self.currency = currency

