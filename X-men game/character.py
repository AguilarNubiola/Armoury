from power import claws

class mutant:
    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health
        self.health_max = health

        self.power = claws

    
    def attack(self, target) -> None:
        target.health -= self.power.damage
        target.health = max(target.health, 0)
        print(f"{self.name} dealt {self.power.damage} damage to {target.name} with {self.power.name}")


class Hero(mutant):
    def __init__(self, name:str, health: int) -> None:
        super().__init__(name=name, health=health)

class Enemy(mutant):
    def __init__(self, name:str, health:int, power) -> None:
        super().__init__(name=name, health=health)
        self.power = power