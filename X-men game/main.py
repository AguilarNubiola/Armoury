from character import Hero, Enemy, Teammate
from power import birdie, weatherControl

hero = Hero(name="Wolverine", health=100)
enemy = Enemy(name="Sabretooth", health=100, power=birdie)
teammate = Teammate(name="Storm", health=100, power=weatherControl)

while True:
    hero.attack(enemy)
    enemy.attack(hero)
    hero.help(teammate)

    print(f"Health of {hero.name}: {hero.health}")
    print(f"Health of {enemy.name}: {enemy.health}")
    print(f"Health of {teammate.name}: {teammate.health}")

    input()