from tetriumrpg.tile import Tile
from tetriumrpg.enum import Sprite_ID
from tetriumrpg.tmx_loader import TmxLoader
class Map:
    map = []
    
    def __init__(self):
        self.map = self.load_map()
    
    def load_map(self):
        tmx_loader = TmxLoader()
        map = tmx_loader.load_map("game_map")
                
        print("Map Loaded!") 
        return map
       
    def get_tile(self, x, y):
        for tile in self.map:
            if(tile != None):
                if(tile.x == x and tile.y == y):
                    return tile
            
    def render(self, sprite_handler, _display_surf, player_x, player_y):
        for tile in self.map:
            tile.render(sprite_handler, _display_surf, player_x, player_y)