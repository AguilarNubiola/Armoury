class power:
    def __init__(self, name: str, power_type: str, damage: int, value: int) -> None:
        self.name = name
        self.power_type = power_type
        self.damage = damage
        self.value = value

telepathy = power(name='telepathy', power_type = 'telepathy', damage=10, value=10)

optic_blasts = power(name="Optic blasts", power_type="Energy", damage=10, value=10)


claws = power(name="Adamantium claws", power_type="sharp", damage=5, value=5)

birdie = power(name="Birdie's gun", power_type="ballistics", damage=3, value=10)

weatherControl = power(name="Weather manipulation", power_type="Energy manipulation", damage=20, value=10)

magnetism = power(name="Electro-magnetic manipulation", power_type="Energy manipulation", damage=30, value=10)