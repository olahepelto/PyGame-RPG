import os
import pygame

class SpriteHandler:
    sprite_list = {}
    
    def __init__(self):
        self.add_spritesheet("Engineer",4,4,["d1","d2","d3","d4","l1","l2","l3","l4","r1","r2","r3","r4","u1","u2","u3","u4"])
        self.add_spritesheet("Tileset1",18,17,list(range(0, 323)))
    
    def add_spritesheet(self, filename, w, h, sprite_names): # w, h = width,height / 16
        spritesheet = pygame.image.load(os.path.join(os.path.dirname(__file__), "..\sprites\\" + filename + ".bmp"))
        sprites = {}
        
        i = 0
        y = 0
        while y < h:
            x = 0
            while x < w:
                sprites[sprite_names[i]] = spritesheet.subsurface(x*16,y*16,16,16)
                i += 1
                x += 1
            y += 1
            
        self.sprite_list[filename] = sprites
        
    def get_sprite(self, sheet_name, sprite_name):
        return self.sprite_list[sheet_name][sprite_name]