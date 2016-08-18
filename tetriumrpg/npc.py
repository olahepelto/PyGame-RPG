class NPC:
    
    def __init__(self, name, x, y, drop, sprite, health, movement_pattern):
        self.name = name
        self.x = x
        self.y = y
        self.loot = drop
        self.sprite = sprite
        self.health = health
        self.movement_pattern = movement_pattern #ex. MovementPattern.Generic
    
    def hit(self, damage):
        self.health -= damage
    
    def talk(self):
        pass
        #Create dialogue(Not implemented yet)