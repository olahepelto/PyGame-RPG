from enum import Window_Definitions
import pygame

class Tile:
    x = 0
    y = 0
    sprite = 0
    spritesheet_name = 0
    metadata = 0
    myfont = 0
    
    def __init__(self, x, y, sprite, metadata): #x, y center
        self.x = x
        self.y = y
        self.sprite = sprite
        self.spritesheet_name = "Tileset1"
        self.metadata = metadata
        self.myfont = pygame.font.SysFont("comicsansms", 18)
        
    def render(self, sprite_handler, _display_surf, player_x, player_y):

        #The pygame render library works differently than i orginally imagined the map to work
        #Thats why the x and y are reversed a bit
        tile_x = (self.y*32 + Window_Definitions.Window_Width/2) - player_x
        tile_y = (self.x*32 + Window_Definitions.Window_Height/2) - player_y
        
        _display_surf.blit(pygame.transform.scale(sprite_handler.get_sprite(self.spritesheet_name,self.sprite), (32,32)),(tile_x,tile_y))
        
        #if(self.metadata["restricted"]):
            #label = self.myfont.render("B", 1, (255,0,0))
            #_display_surf.blit(label, (tile_x + 2, tile_y + 2))