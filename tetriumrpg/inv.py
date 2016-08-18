from pygame import Color
import pygame

class Inv:
    contents = []
    selected = 0
    
    #Inventory Layout
    #
    # 0  1  2  3  4  5  6
    # 7  8  9 10 11 12 13
    # 14 15 16 17 18 19 20
    # 21 22 23 24 25 26 27
    # 28 29 30 31 32 33 34
    #
    
    def __init__(self, contents):
        self.contents = contents #Index = See inventory layout
        self.selected = 0
        
    def add_stack(self, item_stack):
        if("" in self.contents):
            contents[self.contents.index("")] = item_stack
        else:
            if(len(self.contents) < 35):
                contents.append(item_stack)
    
    def modify_stack(self, slot, new_stack):
        self.contents[slot] = new_stack
    
    def del_stack(self, slot):
        self.contents[slot] = ""
    
    def render(self, sprite_handler, _display_surf):
        for i in range(0,8):
            if(i == self.selected):
                pygame.draw.rect(_display_surf, Color(255,255,255), [18 + 40 * i + 32,50,32,32], 2)
            else:
                pygame.draw.rect(_display_surf, Color(0,0,0), [18 + 40 * i + 32,50,32,32], 2)
                
    def select(self, select_id):
        self.selected = select_id - 1