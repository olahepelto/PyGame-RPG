from enum import Location, ID, Sprite_ID, Window_Definitions
import os

import pygame
from pygame.locals import *

from entity import Entity
from entity_handler import EntityHandler
import entity_handler, sprite_handler
from map import Map
from player import Player
from renderer import Renderer
from sprite_handler import SpriteHandler
from ticker import Ticker
from tmx_loader import TmxLoader
from inv import Inv


class App:
    tps = 24
    fps = 25
       
    sprite_handler = 0
    entity_handler = 0
    
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
 
    def on_init(self):
        pygame.init()

        self._display_surf = pygame.display.set_mode((Window_Definitions.Window_Width,Window_Definitions.Window_Height), pygame.HWSURFACE)
        pygame.display.set_caption('Tetrium RPG')
        self._running = True
 
    def on_event(self, event):
        pass
            
    def on_cleanup(self):
        pygame.mixer.quit()
        pygame.quit()
        
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
        
        pygame.mixer.init()
        pygame.mixer.music.load(os.path.join(os.path.dirname(__file__), "..\sound\\Pixelland.wav"))
        
        pygame.mixer.music.play(-1)
        
        tmx_loader = TmxLoader()
        map = tmx_loader.load_map("game_map")
        
        sprite_handler = SpriteHandler()
        entity_handler = EntityHandler(tmx_loader)
        map = Map(map)
        player = Player(Location.Spawn, ID.Player, "Engineer", Sprite_ID.Player_d4, map)
        inv = Inv(None)
        entity_handler.add_entity(player)
        
        renderer = Renderer(entity_handler, sprite_handler, self._display_surf)
        ticker = Ticker(entity_handler, self)
        
        time_next_tick = 0
        time_next_render = 0
        tick = 0
        render = 0
        nextsecond = 0
        while(self._running):
            time_now = pygame.time.get_ticks()
            
            if(time_now > time_next_tick):
                ticker.tick()
                time_next_tick = time_now + 1000 / self.tps
                tick += 1
                
            if(time_now > time_next_render):
                renderer.render(entity_handler, map, inv)
                time_next_render = time_now + 1000 / self.fps
                render += 1
                    
            if(nextsecond < time_now):
                print("TPS: " + str(tick) + " FPS: " + str(render))
                tick, render = 0,0
                nextsecond = time_now + 1000
            
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()