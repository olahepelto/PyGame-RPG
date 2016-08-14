from entity import Entity
import pygame
import tetriumrpg
from tetriumrpg.enum import Window_Definitions
import math


class Player(Entity):
    walk_anim_speed = 140
    last_anim = 0
    
    def __init__(self, location, entity_id, spritesheet, def_sprite_id, map):
        super().__init__(location, entity_id, spritesheet, def_sprite_id, map)
        
    def moveRight(self):
        tile_right = self.get_tile_restricted("r")
        
        if(tile_right == True):
            if(math.floor(self.x/32) > self.x/32):
                self.x = self.x + self.speed
                self.anim_walk("r")
        else:
            self.x = self.x + self.speed
            self.anim_walk("r")
    def moveLeft(self):
        tile_left = self.get_tile_restricted("l")
        
        if(tile_left == True):
            if(math.ceil(self.x/32) < self.x/32):
                self.x = self.x - self.speed
                self.anim_walk("l")
        else:
            self.x = self.x - self.speed
            self.anim_walk("l")
        
    def moveUp(self):
        tile_up = self.get_tile_restricted("u")
        
        if(tile_up == True):
            if(math.ceil(self.y/32) < self.y/32):
                self.y = self.y - self.speed
                self.anim_walk("u")
        else:
            self.y = self.y - self.speed
            self.anim_walk("u")
        
    def moveDown(self):
        tile_down = self.get_tile_restricted("d")
        
        if(tile_down == True):
            if(math.floor(self.y/32) > self.y/32):
                self.y = self.y + self.speed
                self.anim_walk("d")
        else:
            self.y = self.y + self.speed
            self.anim_walk("d")
        
    def anim_walk(self, dir):
        self.set_dir(dir)
        time_now = pygame.time.get_ticks()
        if(self.last_anim + self.walk_anim_speed < time_now):
            self.next_sprite()
            self.last_anim = time_now
    
    def render(self, sprite_handler, _display_surf):
        _display_surf.blit(pygame.transform.scale(sprite_handler.get_sprite(self.spritesheet_name,self.sprite_id), (32,32)),(Window_Definitions.Window_Width/2,Window_Definitions.Window_Height/2))
        
        myfont = pygame.font.SysFont("comicsansms", 30)
        
        coordinates = myfont.render(str(int(self.x)/32) + " " + str(int(self.y)/32), 1, (255,0,0))
        _display_surf.blit(coordinates, (5, 5))
        
    def get_tile_restricted(self, dir):
            if(dir == "r"):
                return self.map.get_tile(round(self.y/32), round(self.x/32 + 0.5)).metadata["restricted"]
            if(dir == "l"):
                return self.map.get_tile(round(self.y/32), round(self.x/32 - 0.5)).metadata["restricted"]
            if(dir == "d"):
                return self.map.get_tile(round(self.y/32 + 0.5), round(self.x/32)).metadata["restricted"]
            if(dir == "u"):
                return self.map.get_tile(round(self.y/32 - 0.5), round(self.x/32)).metadata["restricted"]
            
        
        
        