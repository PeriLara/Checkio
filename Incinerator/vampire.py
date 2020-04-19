# Taken from mission The Defenders

# Taken from mission Army Battles

# Taken from mission The Warriors

class Warrior:
    
    def __init__(self):
        self.health = 50
        self.attack = 5
        
    def __repr__(self):
        return f"health: {self.health} is_alive: {self.is_alive}"
        
    @property
    def is_alive(self):
        return self.health > 0
        
    def attacking(self, other_unit):
        print("b", self.health, other_unit.health)
        other_unit.defending(self)
        print("a", self.health, other_unit.health)
        
    def defending(self, enemy):
        self.health -= enemy.attack
        return enemy.attack

class Knight(Warrior):
    
    def  __init__(self):
        super().__init__()
        self.attack += 2
    
    def __repr__(self):
        return  f"{super().__repr__()} -- Knight"
    
        
class Defender(Warrior):
    
    def __init__(self):
        super().__init__()
        self.health += 10
        self.attack -= 2
        self.defense = 2
        
    def __repr__(self):
        return  f"{super().__repr__()} -- Defender"
        
    def defending(self, ennemy):
        damage = ennemy.attack - self.defense
        if damage > 0:
            self.health -= damage
        return damage
        
class Vampire(Warrior):
    
    def __init__(self):
        super().__init__()
        self.health -= 10
        self.attack -= 1
        self.vampirism = 50
    
    def __repr__(self):
        return  f"{super().__repr__()} -- Vampire"
        
    def attacking(self, other_unit):
        dealt_damage = other_unit.defending(self)
        print("dealt damage", dealt_damage)
        print(self.health)
        self.health += dealt_damage * (self.vampirism / 100)
        print(self.health)
    
class Army:
    
    def __init__(self):
        self.units = []
        
    def __repr__(self):
        representation = "Army : \n"
        for unit in self.units:
            representation += unit.__repr__() + "\n"
        return  representation
        
    @property
    def fighters(self):
        return len(self.units)
    
    def are_alive(self):
        print([element.is_alive for element in self.units])
        print(any(element.is_alive for element in self.units))
        return any(element.is_alive for element in self.units)
        
    def add_units(self, unit, number):
        self.units.extend([unit() for _ in range(number)])

            
class Battle:
    
    def __init__(self):
        pass
        
    def fight(self, army_1, army_2):
        while army_1.are_alive() and army_2.are_alive():
            fighters_1 = army_1.units[0]
            fighters_2 = army_2.units[0]
            if fight(fighters_1, fighters_2):
                army_2.units.pop(0)
            else:
                army_1.units.pop(0)
        return army_1.are_alive()

def fight(unit_1, unit_2):
    print(unit_1, unit_2)
    while unit_1.is_alive and unit_2.is_alive:
        unit_1.attacking(unit_2)
        if unit_2.is_alive:
            print("unit2 is alvie")
            unit_2.attacking(unit_1)
        else:
            print("unit2 dead")

        
    return unit_1.is_alive
        

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    """
    #fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()
    eric = Vampire()
    adam = Vampire()
    richard = Defender()
    ogre = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True
    assert fight(eric, richard) == False
    assert fight(ogre, adam) == True

    #battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Warrior, 1)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 4)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")"""
    
    army_1 = Army()
    army_2 = Army()
    army_1.add_units(Defender, 11)
    army_1.add_units(Vampire, 3)
    army_1.add_units(Warrior, 4)
    army_2.add_units(Warrior, 4)
    army_2.add_units(Defender, 4)
    army_2.add_units(Vampire, 13)
    
    print(army_1)
    
    print(army_2)
    
    battle = Battle()
    print(battle.fight(army_1, army_2))
    