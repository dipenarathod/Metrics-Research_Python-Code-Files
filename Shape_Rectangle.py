class Shape:
    """Base class for all shapes."""
    
    def __init__(self, name):
        self.name = name
    
    def area(self):
        """Calculate the area of the shape."""
        return 0
    
    def perimeter(self):
        """Calculate the perimeter of the shape."""
        return 0
    
    def describe(self):
        """Return a description of the shape."""
        return f"This is a {self.name} with area {self.area()} and perimeter {self.perimeter()}."


class Rectangle(Shape):
    """Rectangle shape class."""
    
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height
    
    def area(self):
        """Calculate the area of the rectangle."""
        return self.width * self.height
    
    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        return 2 * (self.width + self.height)