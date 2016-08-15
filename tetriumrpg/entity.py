import pygame
from enum import Animation, Window_Definitions


class Entity(object):
    speed = 0
    x = 0
    y = 0
    dir = "d"
    entity_id = -1
    spritesheet_name = 0
    sprite_id = 0
    anim_stage = 1
    map = None
    
    def __init__(self, location, entity_id, spritesheet_name, def_sprite_id, map):
        self.x = location[0]
        self.y = location[1]
        self.entity_id = entity_id
        self.sprite_id = def_sprite_id #DEFAULT
        self.spritesheet_name = spritesheet_name
        self.speed = 5
        self.map = map
        
    def render(self, sprite_handler, _display_surf):
        ##
        ## Have to take into account how the player moves
        ##
        _display_surf.blit(pygame.transform.scale(sprite_handler.get_sprite(self.spritesheet_name,self.sprite_id), (32,32)),(self.x*32,self.y*32))
    
    def set_sprite(self, sprite_id):
        self.sprite_id = sprite_id
    
    def next_sprite(self):
        found = False
        
        for anim in Animation.Player[self.dir]:
            for spr_name in anim:
                if(spr_name == self.sprite_id):
                    found = True
                    break
            if(found):
                break
            
        if(self.anim_stage > len(spr_name)+2):
            self.anim_stage = 1
        else:
            self.anim_stage += 1
            
        self.set_sprite(self.dir + str(self.anim_stage))
    
    def set_dir(self, dir):
        self.dir = dir
    
    def reset_sprite(self):
        self.set_sprite(self.dir + "1")