class Villager:
    def __init__(self, name):
        self.name = name
        self.health = 50
        self.defense = 0
        self.attack = 0
        self.is_alive = True


    def check_health(self, incoming_attack_value):
        damage = incoming_attack_value - self.defense

        self.health -= damage
        self.health = self.health if self.health > 0 else 0
        if not self.health:
            self.is_alive = False
            return (False, 'target is dead ):')
        return self.health

    
    def normal_attack(self, target):
        return target.check_health(self.attack)


