import uuid
import random
from helpers import quality_generator
from _types import Stat


class Weapon:
    def __init__(self, name: str, stat: Stat, durability: int, required_level: int, damage: int, effect: str, currency: int):
        self.id = uuid.uuid4()
        self.name = name
        self.stat = stat
        self.durability = durability
        self.required_level = required_level
        self.quality = quality_generator()
        self.damage = damage
        self.effect = effect
        self.currency = currency


a = Weapon("dwjad", "strength", 30, 45, 39, "none", 400)
b = Weapon("dwjad", "strength", 30, 45, 39, "none", 400)
