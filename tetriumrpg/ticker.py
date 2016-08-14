import pygame
from pygame.locals import *
from tetriumrpg.enum import ID

class Ticker:
    
    def __init__(self, entity_handler, game):
        self.entity_handler = entity_handler
        self.game_instance = game
    
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
        
        if(right_down == False and left_down == False and up_down == False and down_down == False):
            player.reset_sprite()
