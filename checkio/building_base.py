class Building:
    def __init__(self, south, west, width_WE, width_NS, height = 10):
        self.south = south
        self.west = west
        self.width_WE = width_WE
        self.width_NS = width_NS
        self.height = height
    

    def corners(self):
        corners['north-west'] = [3, 2]
        
