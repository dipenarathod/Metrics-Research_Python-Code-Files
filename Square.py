from Shape_Rectangle import Rectangle
class Square(Rectangle):
    """Square shape class."""
    
    def __init__(self, side):
        super().__init__(side, side)
        self.name = "Square"