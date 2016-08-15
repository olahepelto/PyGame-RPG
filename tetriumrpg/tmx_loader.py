import os
from tile import Tile

class TmxLoader:
    map_heigth ={}
    
    def __init__(self):
        pass

    def read_csv(self, csv_str):
        raw_csv = self.find_between(csv_str, "<data encoding=\"csv\">", "</data>")
        return raw_csv

    def get_width_heigth(self, x, csv_str):
        w = self.find_between(csv_str, "<map version=\"1.0\" orientation=\"orthogonal\" renderorder=\"right-down\" width=\"", "\" height=\"")
        h = self.find_between(csv_str, "<map version=\"1.0\" orientation=\"orthogonal\" renderorder=\"right-down\" width=\"" + w + "\" height=\"", "\" tilewidth=")
        
        return [w, h]
    
    def get_tile_metadata(self, xml_data):
        data2 = []
        prop_list = []
        
        xml_data = self.find_between(xml_data, "<image source=\"Tiles/Tileset1.bmp\" width=\"288\" height=\"288\"/>", "</tileset>")
        
        for i,data in enumerate(xml_data.split("</tile>")):
            try:
                data = self.find_between(data, "<properties>", "</properties>")
            except Exception:
                pass
            
            data = data.split("/>")
            
            prop_list = []
            for prop in data:
                prop = prop.replace("\n", "").replace("  ","").replace("<property ", "")
                prop_list.append(prop)
            
            data2.append(prop_list)
        
        data = []
        for i,str in enumerate(data2):
            if(str != " "):
                data.append(str)


        d3 = []
        dattta = []
        for d in data:
            d.pop(-1)
            
            dremove_slashes = []
            for d2 in d:
                dremove_slashes.append(d2.replace("\"",""))
            d = dremove_slashes
            
            dank_memes = []
            for d2 in d:
                d3 = d2.split(" ")
                
                thingy = {}
                for d4 in d3: #d4 = name=restricted OR type=bool OR value=false
                    d5 = d4.split("=")
                    
                    if(d5[0] == "name"):
                        name = d5[1]
                    if(d5[0] == "value"):
                        value = d5[1]
                        if(value == "true"):
                            value = True
                        if(value == "false"):
                            value = False
                            
                thingy[name] = value
                dank_memes.append(thingy)
            dattta.append(dank_memes)
        return dattta
    
    def get_objects(self, filename):
        objects = []
        new_obj = {}
        
        tmx_file = open(os.path.join(os.path.dirname(__file__), "..\maps\\" + filename + ".tmx"), "r")
        tmx_file = tmx_file.read()
        
        xml_data = self.find_between(tmx_file, "<objectgroup name=\"Objects\">", " </objectgroup>")
        xml_data = xml_data.split("\n")
        xml_data.pop(-1)#Delete Last Item -> ''
        xml_data.pop(0)#Delete First Item -> ''
        
        objects = self.get_xml_attr(xml_data)
        
        return objects
    
    def find_between(self, s, first, last):
            start = s.index(first) + len(first)
            end = s.index(last, start)
            return s[start:end]
        
    def get_xml_attr(self,xml):
        new_obj = {}
        objects = []
        
        for obj in xml:
            obj = self.find_between(obj, "  <object ", "/>").split(" ")
            
            new_obj = {}
            
            for attr in obj:
                attr = attr.replace("\"", "").split("=")
                
                if(attr[0] == "gid"):
                    attr[0] = "entity_id"
                new_obj[attr[0]] = attr[1]
                
                        
                #<object id="17" gid="61" x="800" y="880" width="16" height="16"/>
                
            objects.append(new_obj)
        print(objects)
        return objects
    
    def load_map(self, filename):
        tile_list = []
        map = []
        
        tmx_file = open(os.path.join(os.path.dirname(__file__), "..\maps\\" + filename + ".tmx"), "r")
        tmx_file = tmx_file.read()
        
        tile_metadata = self.get_tile_metadata(tmx_file)
        
        tile_list = self.read_csv(tmx_file).split(",")
        
        map_width = int(self.get_width_heigth(self, tmx_file)[0])
        map_heigth = int(self.get_width_heigth(self, tmx_file)[1])
            
        i = 0
        for x in range(0,map_width):
            for y in range(0,map_heigth):
                if tile_list[i].startswith('\n'):
                    tile_list[i] = tile_list[i][1:]
                tile_list[i] = int(tile_list[i]) - 1
                map.append(Tile(x, y, tile_list[i], tile_metadata[tile_list[i]][0])) # -1 to sprite_id to repair weird bug
                i += 1
        return map