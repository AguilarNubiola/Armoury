from character import Hero, Enemy
from power import birdie,  pheromones

hero = Hero(name="Daken", health=100)
hero.activate(pheromones)
enemy = Enemy(name="Sabretooth", health=100, power=birdie)

while True:
    hero.attack(enemy)
    enemy.attack(hero)

    

    hero.health_bar.draw()
    enemy.health_bar.draw()

    input()