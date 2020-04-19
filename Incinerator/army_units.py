class Army:
    
    def __init__(self):
        pass
        
    def train_swordsman(self, name):
        return Swordsman(name, self)
    
    def train_lancer(self, name):
        return Lancer(name, self)
    
    def train_archer(self, name):
        return Archer(name, self)
        
class Unit:
    
    def __init__(self, name, army):
        self.name = name 
        self.army = army

class Swordsman(Unit):
    def __init__(self, name, army):
        super().__init__(name, army)
        
    def introduce(self):
        return f"{self.army.swordsman_name} {self.name}, {self.army.army_type} swordsman"
        

class Lancer(Unit):
    def __init__(self, name, army):
        super().__init__(name, army)
    
    def introduce(self):
        return f"{self.army.lancer_name} {self.name}, {self.army.army_type} lancer"

class Archer(Unit):
    def __init__(self, name, army):
        super().__init__(name, army)
        
    def introduce(self):
        return f"{self.army.archer_name} {self.name}, {self.army.army_type} archer"

class AsianArmy(Army):
    
    def __init__(self):
        super().__init__()
        self.swordsman_name = "Samurai"
        self.lancer_name = "Ronin"
        self.archer_name = "Shinobi" 
        self.army_type = "Asian"
        
class EuropeanArmy(Army):
    
    def __init__(self):
        super().__init__()
        self.swordsman_name = "Knight"
        self.lancer_name = "Raubritter"
        self.archer_name = "Ranger"
        self.army_type = "European"
    
    



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    my_army = EuropeanArmy()
    enemy_army = AsianArmy()

    soldier_1 = my_army.train_swordsman("Jaks")
    soldier_2 = my_army.train_lancer("Harold")
    soldier_3 = my_army.train_archer("Robin")

    soldier_4 = enemy_army.train_swordsman("Kishimoto")
    soldier_5 = enemy_army.train_lancer("Ayabusa")
    soldier_6 = enemy_army.train_archer("Kirigae")

    assert soldier_1.introduce() == "Knight Jaks, European swordsman"
    assert soldier_2.introduce() == "Raubritter Harold, European lancer"
    assert soldier_3.introduce() == "Ranger Robin, European archer"
    
    assert soldier_4.introduce() == "Samurai Kishimoto, Asian swordsman"
    assert soldier_5.introduce() == "Ronin Ayabusa, Asian lancer"
    assert soldier_6.introduce() == "Shinobi Kirigae, Asian archer"

    print("Coding complete? Let's try tests!")

