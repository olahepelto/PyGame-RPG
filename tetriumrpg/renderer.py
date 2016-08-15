import pygame
from enum import ID
import sprite_handler

class Renderer:
    
    def __init__(self, entity_handler, sprite_handler, _display_surf):
        self.sprite_handler = sprite_handler
        self._display_surf = _display_surf

    def render(self, entity_handler, map):
        self._display_surf.fill((0,0,0))
        
        player_x = entity_handler.get_entity(ID.Player).x
        player_y = entity_handler.get_entity(ID.Player).y
        
        map.render(self.sprite_handler, self._display_surf, player_x, player_y)
        entity_handler.render(self.sprite_handler, self._display_surf)    
        pygame.display.flip()