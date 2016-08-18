class ID:
    Player = 1
    Square = 2

class Location:
    Spawn = [50*32,50*32]
    
class Sprite_ID:
    ##########
    #Engineer#
    ##########
    
    Player_d1 = "d1"
    Player_d2 = "d2"
    Player_d3 = "d3"
    Player_d4 = "d4"
    Player_l1 = "l1"
    Player_l2 = "l2"
    Player_l3 = "l3"
    Player_l4 = "l4"
    Player_r1 = "r1"
    Player_r2 = "r2"
    Player_r3 = "r3"
    Player_r4 = "r4"
    Player_u1 = "u1"
    Player_u2 = "u2"
    Player_u3 = "u3"
    Player_u4 = "u4"
    
    ########
    #floor1#
    ########
    
    grass_nw = 0
    grass_n = 1
    grass_ne = 2
    stone_nw = 3
    stone_n = 4
    stone_ne = 5
    floor_nw = 6
    floor_n = 7
    floor_ne = 8      
    grass_w = 9
    grass = 10
    grass_e = 11
    stone_w = 12
    stone = 13
    stone_e = 14
    floor_w = 15
    floor = 16
    floor_e = 17
    grass_sw = 18
    grass_s = 19
    grass_se = 20
    stone_sw = 21
    stone_s = 22
    stone_se = 23
    floor_sw = 24
    floor_s = 25
    floor_se = 26
    
    sandpit_nw = 27
    sandpit_n = 28
    sandpit_ne = 29
    
    sandwhite_nw = 30
    sandwhite_n = 31
    sandwhite_ne = 32
    
class Animation:
    Player = {"d":["d1","d2","d3","d4"],"l":["l1","l2","l3","l4"],"r":["r1","r2","r3","r4"],"u":["u1","u2","u3","u4"]}

class Window_Definitions:
    Window_Width = 1200
    Window_Height = 800

class MovementPattern:
    Generic = 0