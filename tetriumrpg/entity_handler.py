class EntityHandler:
    entity_list = [] 
    def __init__(self):
        pass
    
    def add_entity(self, game_object):
        self.entity_list.append(game_object)
        
    def get_entity(self, find_this_id):
        for ent in self.entity_list:
            if(ent.entity_id == find_this_id):
                return ent
    
    def get_all_entities(self):
        return self.entity_list
    
    def render(self, sprite_handler, _display_surf):
        for entity in self.get_all_entities():
            entity.render(sprite_handler, _display_surf)