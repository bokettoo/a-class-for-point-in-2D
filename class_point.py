
class points:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    
    def seters_x(self,x):
        return self.x == x
    
    def seters_y(self,y):
        return self.y == y
    
    def distance(self, point):
        dx = self.x - point.x
        dy = self.y - point.y
        
        return round((dx**2 + dy**2)**0.5)
    
    def norm(self):
        return round(self.x**2 +self.y**2)**0.5
    

