from power import claws
from health_bar import HealthBar

class mutant:
    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health
        self.health_max = health

        self.power = claws

    
    def attack(self, target) -> None:
        target.health -= self.power.damage
        target.health = max(target.health, 0)
        target.health_bar.update()
        print(f"{self.name} dealt {self.power.damage} damage to {target.name} with {self.power.name}")


class Hero(mutant):
    def __init__(self, name:str, health: int) -> None:
        super().__init__(name=name, health=health)

        self.default_power = self.power
        self.health_bar = HealthBar(self, color="yellow")

    def activate(self, power) -> None:
        self.power = power
        print(f"{self.power} activated {self.power.name}")

    def deactivate(self) -> None:
        self.power = self.default.power
        print(f"{self.name} deactivated {self.power}" )

class Enemy(mutant):
    def __init__(self, name:str, health:int, power) -> None:
        super().__init__(name=name, health=health)
        self.power = power

        self.health_bar = HealthBar(self, color="red")

