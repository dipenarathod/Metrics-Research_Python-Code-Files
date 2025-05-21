from Shape_Rectangle import Shape
class ShapeCalculator:
    """Utility class for performing calculations on shapes."""
    
    def __init__(self):
        self.shapes = []
    
    def add_shape(self, shape):
        """Add a shape to the calculator."""
        if not isinstance(shape, Shape):
            raise TypeError("Object must be a Shape")
        self.shapes.append(shape)
        return len(self.shapes)
    
    def total_area(self):
        """Calculate the total area of all shapes."""
        total = 0
        for shape in self.shapes:
            total += shape.area()
        return total
    
    def average_perimeter(self):
        """Calculate the average perimeter of all shapes."""
        if not self.shapes:
            return 0
        total = sum(shape.perimeter() for shape in self.shapes)
        return total / len(self.shapes)
    
    def find_largest_shape(self):
        """Find the shape with the largest area."""
        if not self.shapes:
            return None
        return max(self.shapes, key=lambda shape: shape.area())
    def find_smallest_shape(self):
        """Find the shape with the smallest area."""
        if not self.shapes:
            return None
        return min(self.shapes, key=lambda shape: shape.area())
