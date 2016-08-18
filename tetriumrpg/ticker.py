import pygame
from pygame.locals import *
from enum import ID

class Ticker:
    
    def __init__(self, entity_handler, game, inv):
        self.entity_handler = entity_handler
        self.game_instance = game
        self.inv = inv
    
    def tick(self):
        pygame.event.pump()
        keys = pygame.key.get_pressed() 
        
        player = self.entity_handler.get_entity(ID.Player)
        
        if (keys[K_RIGHT]):
            player.moveRight()
            right_down = True
        else:
            right_down = False
            
        if (keys[K_LEFT]):
            player.moveLeft()
            left_down = True
        else:
            left_down = False
            
        if (keys[K_UP]):
            player.moveUp()
            up_down = True
        else:
            up_down = False
            
        if (keys[K_DOWN]):
            player.moveDown()
            down_down = True
        else:
            down_down = False
        
        if (keys[K_ESCAPE]):
            self.game_instance._running = False
        
        if (keys[K_0] or keys[K_1] or keys[K_2] or keys[K_3] or keys[K_4] or keys[K_5] or keys[K_6] or keys[K_7] or keys[K_8] or keys[K_9]):
            if(keys[K_0]):
                self.inv.select(0)
            if(keys[K_1]):
                self.inv.select(1)
            if(keys[K_2]):
                self.inv.select(2)
            if(keys[K_3]):
                self.inv.select(3)
            if(keys[K_4]):
                self.inv.select(4)
            if(keys[K_5]):
                self.inv.select(5)
            if(keys[K_6]):
                self.inv.select(6)
            if(keys[K_7]):
                self.inv.select(7)
            if(keys[K_8]):
                self.inv.select(8)
            if(keys[K_9]):
                self.inv.select(9)
            
        
        
        if(right_down == False and left_down == False and up_down == False and down_down == False):
            player.reset_sprite()
