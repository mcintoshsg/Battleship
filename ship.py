
from constants import Constants

class Ship:
    size = 5
    hit_points = size
    ship_class = 'SHIP'
    coordiantes = ''
    orientation = 'v'
    
    def __init__(self, **kwargs):
    	for key, value in kwargs.items():
    		setattr(self, key, value)
