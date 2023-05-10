# Model for pipeline GUI

from copy import deepcopy

class Block():
    def __init__(self, pop_id: int, pop_name: str, start_time: int, end_time: int, pop_size: int):
        self.pop_id = "p" + str(pop_id)
        self.name = pop_name
        self.start_time = start_time
        self.end_time = end_time # -1 if doesnt exist :(
        self.pop_size = pop_size
        self.neighbors = {}
    
    def add_migration(self, migration_to: str, migration_rate: float):
        self.neighbors[migration_to] = migration_rate
        
    def make_children(self, start_time):
        child = deepcopy(self)
        child.start_time = start_time
        return child





