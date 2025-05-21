from Shape_Rectangle import Shape

class Circle(Shape):
    """Circle shape class."""
    
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    
    def area(self):
        """Calculate the area of the circle."""
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        """Calculate the circumference of the circle."""
        import math
        return 2 * math.pi * self.radius