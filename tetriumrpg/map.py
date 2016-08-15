from tile import Tile
from enum import Sprite_ID
from tmx_loader import TmxLoader
class Map:
    map = []
    
    def __init__(self, map):
        self.map = map
        print("Map Loaded!")
        
    def get_tile(self, x, y):
        for tile in self.map:
            if(tile != None):
                if(tile.x == x and tile.y == y):
                    return tile
            
    def render(self, sprite_handler, _display_surf, player_x, player_y):
        for tile in self.map:
            if(abs(tile.x*32) - abs(player_y) < 32*16 and abs(tile.x*32) - abs(player_y) > -32*16 and abs(tile.y*32) - abs(player_x) < 32*20 and abs(tile.y*32) - abs(player_x) > -32*20):
                tile.render(sprite_handler, _display_surf, player_x, player_y)