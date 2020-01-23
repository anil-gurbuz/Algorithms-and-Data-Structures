class Point:

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def distance_from_origin(self):
        return ((self.x**2) + (self.y**2))**0.5

    def distance_to_point(self,p2):
        return ((p2.x - self.x)**2 +(p2.y - self.y)**2)**0.5
